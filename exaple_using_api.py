import mirobot_api as api
import numpy as np
api.homing_sync()#perform homing opteration to unlock motors
api.cf_r(10,10,10,axis5_angle = 5,speed = 2000)#move robot to 10,10,0,5,0 cartisian relative to initial position. with speed 2000
api.check_state_cmd()# sent command to check robot current state
x = 0 # let robot finish
data = api.get_data()#get data from robot store into tuple
print(data[1])#display status: running, idle,error etc.