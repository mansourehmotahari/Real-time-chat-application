var socket = io.connect('http://localhost:80/kafka');
var messages = document.getElementById("messages");

(function() {
  $("form").submit(function(e) {
    let li = document.createElement("li");
	e.preventDefault();
	li.setAttribute("style",'padding:10px; width:75%;float:left;margin-top:20px;background-color: rgb(255, 255, 250);color: rgb(0, 0, 0);')
    e.preventDefault();
    socket.emit("kafkaproducer2", $("#message").val(),"user2");
    messages.appendChild(li).append($("#message").val());
    $("#message").val("");

    return false;
  });

  socket.on("kafkaconsumer2", function(msg){
	let li = document.createElement("li");
	li.setAttribute("style",'padding:10px; width:75%;float:right;margin-top:20px;background-color: rgb(153, 0, 76);color: rgb(255, 255, 255);')
    var messages = document.getElementById("messages");
    messages.appendChild(li).append(msg.data); 
  });
})();
