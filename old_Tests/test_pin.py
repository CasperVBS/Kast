from pinnen import *
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883)

print("Typ /pin,state (bv. /D4,1 of /5,0)")



def PinWrite(pin,state):
    msg = f"/{pin},{state}"
    print(msg)
    client.publish("pins/stuur", msg)




while True:
    time.sleep(0.2)
    PinWrite(led,1)
    time.sleep(0.2)
    PinWrite(led,0)