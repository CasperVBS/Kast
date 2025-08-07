from send import send
def MotorA(steps):
    msg = f"/A,{steps}"
    send(msg)

def MotorB(steps):
    msg = f"/B,{steps}"
    send(msg)

def MotorAB(steps):
    msg = f"/S,{steps}"
    send(msg)

def fan(state):
    if state == True:
        send(f"/F,1")
    elif state == False:
        send(f"/F,0")

def enable(state):
    if state == True:
        send(f"/E,1")
    elif state == False:
        send(f"/E,0")  
