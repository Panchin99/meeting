import frappe

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting", meeting)
    meeting.check_permission("email")

    if meeting.status == "Planned":
        frappe.sendmail(
            recipients=[d.attendee for d in meeting.attendees], 
            sender=frappe.session.user,
            subject=meeting.title,
            message=meeting.inivitation_message, 
            reference_doctype=meeting.doctype,
            reference_name=meeting.name,
            as_bulk=True
        )

        meeting.status = "Invitation Sent"
        meeting.save()

        frappe.msgprint(_("Invitation Sent"))


    else:
        frappe.msgprint(_("Meeting Status must be 'Planned'"))

