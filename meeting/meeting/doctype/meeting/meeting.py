# Copyright (c) 2022, Componix and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):

	#validate is a hook, which is called before
	#saving the document
	def validate(self):

		"""set missing names and de-duplicate"""
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

			if attendee.attendee in found:
				frappe.throw(_("Atendee {0} entered more than once")
				.format(attendee.attendee))
			
			found.append(attendee.attendee)


@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)

	#concatenates by space if it has value
	return " ".join(filter(None, [user.first_name,
	user.middle_name, user.last_name]))