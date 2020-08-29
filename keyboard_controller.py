import mirobot_api as api
import numpy as np
import msvcrt as m

#api.homing_sync()#perform homing opteration to unlock motors
k = '0'
x = 0

while k != b'q' and k!= b'\x03':
    k = m.getch()
    if k == b'a':
        print("x neg")
        api.cf_r(0,10,0,0,0,0)
    elif k == b's':
        print("z neg")
        api.cf_r(0,0,-10,0,0,0)
    elif k == b'd':
        print("x pos")
        api.cf_r(0,-10,0,0,0,0)
    elif k == b'w':
        print("z pos")
        api.cf_r(0,0,10,0,0,0)
    elif k == b'g':
        print("y pos")
        api.cf_r(10,0,0,0,0,0)
    elif k == b'h':
        print("y neg")
        api.cf_r(-10,0,0,0,0,0)
    elif k == b'z':
        print("reset pressed")
        api.homing_sync()
    elif k == b'x':
        print("request state")
        api.check_state_cmd()
    elif k == b'p':
        print("toggle gripper")
        if x == 0:
            x = 1
        else:    
            x = 0
        api.grip(x)
    elif k == b't':
        print("move gripper up")
        api.cf_r(0,0,0,0,-10,0)
    elif k == b'y':
        print("move gripper down")
        api.cf_r(0,0,0,0,10,0)
    else:
        print("error unknown command")
    