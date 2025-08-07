import paho.mqtt.client as mqtt
from time import sleep

def on_message(client,userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

global client
client = mqtt.Client()

def send_setup():
     
    client.connect("localhost",1883)
    client.subscribe("kast")
    client.on_message = on_message
    client.loop_start()

def send(msg):
    client.publish("kast",msg)
