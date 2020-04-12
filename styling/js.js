"use strict";


$(document).ready(function() {
	const whereTheNotesGo = $('#allTheNotes');

	$('#addNoteForm').submit(function(event) {
		event.preventDefault();
		const formData = $(this).serializeArray()
		const payload = {
			data: { note: formData[0].value },
			method: 'POST',
			url: '/add_note'
		};
		const myRequest = $.ajax(payload);

		myRequest.then(function(response) {
			const htmlToAdd = `<p>${response.note}</p>` //can add href here
                      									//template literal
			whereTheNotesGo.append(htmlToAdd);

			$('#note').val('')
		})

	});
});