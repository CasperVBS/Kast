from send import send, send_setup
from Arduino_control import MotorA, MotorAB, MotorB
from time import sleep
import paho.mqtt.client as mqtt

send_setup()


def Cordinate(coordinaat):
    x , y = coordinaat
    print(x,y)

def Besturing(command):
    if command == "Left-up":
        print("heoifhzoeufhzoefh")
    elif command =="up":
        print(1)
    elif command =="right-up":
        print(2)
    elif command =="left":
        print(3)
    elif command =="home":
        print(4)
    elif command =="right":
        print(5)
    elif command =="left-down":
        print(6)
    elif command =="down":
        print(7)
    elif command =="right-down":
        print(8)


"""
while True:
    send(f"/F,1")
    MotorAB(1000)
    sleep(2.5)
    send(f"/F,1")
    MotorA(1000)
    sleep(2.5)
    send(f"/F,1")
    MotorB(1000)
    sleep(2.5)"""