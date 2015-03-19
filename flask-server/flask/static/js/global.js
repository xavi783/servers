
$('#enviar').click(function(e){
	e.preventDefault()
	r = {};
	$.map($('#step_values').serializeArray(), function(el,i){ r[el['name']]=el['value']; });
	$.ajax({'url': '/set_intervals/', 'data': r, 'type': 'POST'}).done(alert('sucess'));
	return False;
});