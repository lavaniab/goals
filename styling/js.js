"use strict";


$(document).ready(function() {
	const whereTheGoalsGo = $('#allTheGoals');

	$('#addGoalForm').submit(function(event) {
		event.preventDefault();
		const formData = $(this).serializeArray()
		const payload = {
			data: { goal: formData[0].value },
			method: 'POST',
			url: '/add_goal'
		};
		const myRequest = $.ajax(payload);

		myRequest.then(function(response) {
			const htmlToAdd = `<p>${response.goal}</p>` //can add href here
                      									//template literal
			whereTheGoalsGo.append(htmlToAdd);

			$('#note').val('')
		})

	});
});