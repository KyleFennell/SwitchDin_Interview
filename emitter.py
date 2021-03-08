import paho.mqtt.client as mqtt
import random

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+connack_string(rc))


mqtt_client = mqtt.Client()
# connecting the paho mqtt client to the mqtt server
mqtt_client.connect('localhost', 1883, 60)
message = str(random.randint(1, 100))
# publishing to the rng topic
mqtt_client.publish('rng', message)
print("Sent %r" % message)
mqtt_client.disconnect()

# doing the same for the websocket port to allow the js to receive the message but it produces a websocket handshake error 
# and feel as though I have exhausted all avenues other than asking you for help again but it's too late now. hopefully it 
# is a simple fix

# ws_client = mqtt.Client(transport="websockets")
# ws_client.on_connect = on_connect
# ws_client.ws_set_options(path="/mqtt")
# ws_client.connect('localhost', 15675, 60)
# ws_client.publish('rng', message)
# print("Sent %r" % message)
# ws_client.disconnect()