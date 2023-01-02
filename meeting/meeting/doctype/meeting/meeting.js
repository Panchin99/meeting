// Copyright (c) 2022, Componix and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Meeting Attendee',{
	//frm - FrappeForm Object
	//cdt Child Doctype
	//cdn Child Docname
	attendee: function(frm, cdt, cdn){
		//using the model.get_doc gives us the local/browser version of the attendee
		var attendee = frappe.model.get_doc(cdt, cdn);
		if(attendee.attendee){
			//if attendee, get full name
			frm.call({
				method: "meeting.meeting.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});
		} else{
			//if no attnendee, clear full name
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	}
})