/** paho setup taken mostly from the paho js getting started section. No use rewriting the wheel **/

// Create a client instance
let client = new Paho.MQTT.Client("localhost", Number(15675), "/ws", "clientId");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  client.subscribe("rng");
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  console.log("onMessageArrived:"+message.payloadString);
  // everything goes through number test for now so it is at least testable because the sockets arent working for me
  $('#numbertest').val(parseInt(message.payloadString));
  $('#numbertest').change();
}

$(document).ready(() => {
  $('#numbertest').on('change', function(){
    let that = this;    
    $('#box').velocity({
      height: $(that).val(),
      top: 100-$(that).val()    // an attempt to make the box grow from the bottom
    });
  });
});