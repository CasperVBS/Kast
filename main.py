from send import send, send_setup
from Arduino_control import MotorA, MotorAB, MotorB
from time import sleep
import paho.mqtt.client as mqtt

send_setup()


while True:
    send(f"/F,1")
    MotorAB(1000)
    sleep(2.5)
    send(f"/F,1")
    MotorA(1000)
    sleep(2.5)
    send(f"/F,1")
    MotorB(1000)
    sleep(2.5)