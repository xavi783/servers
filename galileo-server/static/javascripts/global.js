
var ws = new WebSocket("ws://192.168.0.204:8888/websocket");

$("#light").click(function(e){
	e.preventDefault()
	$.ajax({
		'url': '/turn_light/',
		'type': 'GET'})
	.success( function(obj){
		console.log(obj.data)
		light_elem = $("a[href='/turn_light/']")[0]
		if(obj.data=="on" & !light_elem.classList.contains("light_on")){
			light_elem.classList.add("light_on")
		}
		if(obj.data=="off" & light_elem.classList.contains("light_on")){
			light_elem.classList.remove("light_on")
		}
	});
	return False;
});

/*
$('#req-img').click(function(e){
	e.preventDefault()
	ws.send(JSON.stringify(r))
});
*/

var ctx = document.getElementById("my_canvas").getContext("2d");
var image = new Image();
ws.onmessage = function(evt){
	data = JSON.parse(evt.data)
	if(data.src!="data:image/png;base64," && data.src!=""){
		image.src = data.src;
		image.onload = function() {
			ctx.drawImage(image, 0, 0, 320, 240);
		};
        }
};
