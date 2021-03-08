import paho.mqtt.client as mqtt_client
import random


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # generating a pseudo random client id
    client = mqtt_client.Client(f'python-mqtt-{random.randint(0, 100)}');
    client.on_connect = on_connect
    # connecting to the mqtt server
    client.connect('localhost', 1883, 60)
    return client


def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")    


client = connect_mqtt()
client.on_message = on_message
client.subscribe('rng')

client.loop_forever()