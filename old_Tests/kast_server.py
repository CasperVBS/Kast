import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("esp/naar/pi")
client.on_message = on_message
client.loop_start()

while True:
    msg = input("Typ een bericht aan de ESP: ")
    client.publish("pi/naar/esp", msg)
