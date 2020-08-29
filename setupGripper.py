import mirobot_api as api
import numpy as np
#import time
data = api.get_data()
api.homing_sync()#perform homing opteration to unlock motors
#time.sleep(30)
data = api.get_data()
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[6])
print(data[7])
print(data[8])
api.amm_r(axis6_angle = 20,speed = 2000)#move robot to 10,10,0,5,0 cartisian relative to initial position. with speed 2000
api.check_state_cmd()# sent command to check robot current state
x = 0 # let robot finish
data = api.get_data()#get data from robot store into tuple
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[6])
print(data[7])
print(data[8])
#time.sleep(30)
api.amm_r(axis6_angle = 20,speed = 2000)#move robot to 10,10,0,5,0 cartisian relative to initial position. with speed 2000
api.check_state_cmd()# sent command to check robot current state
x = 0 # let robot finish
data = api.get_data()#get data from robot store into tuple
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[6])
print(data[7])
print(data[8])
