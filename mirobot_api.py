import numpy as np
import time

def check_state_cmd():
#"""
#returns the command to request data from mirobot
#"""  
    cmd = "?\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(0.5)
    
def amm_ab(axis1_angle, axis2_angle, axis3_angle, axis4_angle, axis5_angle, axis6_angle, speed = 1000):
#"""
#move robot motors to specified angle
#if no motion is desired for a specific motor the function expects the value np.nan for that parameter
#"""
    cmd = "M21 G90"
    if not np.isnan(axis1_angle):
        cmd = cmd + " X" + str(axis1_angle)
    if not np.isnan(axis2_angle):
        cmd = cmd + " Y" + str(axis2_angle)
    if not np.isnan(axis3_angle):
        cmd = cmd + " Z" + str(axis3_angle)
    if not np.isnan(axis4_angle):
        cmd = cmd + " A" + str(axis4_angle)
    if not np.isnan(axis5_angle):
        cmd = cmd + " B" + str(axis5_angle)
    if not np.isnan(axis6_angle):
        cmd = cmd + " C" + str(axis6_angle)    
    cmd = cmd + " F" + str(speed) + "\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1    
    time.sleep(1)
    
def amm_r(axis1_angle = 0, axis2_angle = 0,axis3_angle = 0, axis4_angle = 0, axis5_angle = 0, axis6_angle = 0, speed = 1000):
#"""
#angle motor motion relatvie to current position
#"""
    cmd = "M21 G91 X" + str(axis1_angle) + " Y" + str(axis2_angle) + " Z" + str(axis3_angle) + " A" + str(axis4_angle) \
    + " B" + str(axis5_angle) + " C" + str(axis6_angle) + " F" + str(speed) + "\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(5)
def cf_ab(axis1_angle, axis2_angle, axis3_angle, axis4_angle, axis5_angle, axis6_angle, speed = 1000):
#"""
#move robot motors to specified cartiesian coordinates fast

#if no motion is desired for a specific motor the function expects the value np.nan for that parameter
#"""
    cmd = "M20 G90 G0"
    if not np.isnan(axis1_angle):
        cmd = cmd + " X" + str(axis1_angle)
    if not np.isnan(axis2_angle):
        cmd = cmd + " Y" + str(axis2_angle)
    if not np.isnan(axis3_angle):
        cmd = cmd + " Z" + str(axis3_angle)
    if not np.isnan(axis4_angle):
        cmd = cmd + " A" + str(axis4_angle)
    if not np.isnan(axis5_angle):
        cmd = cmd + " B" + str(axis5_angle)
    if not np.isnan(axis6_angle):
        cmd = cmd + " C" + str(axis6_angle)    
    cmd = cmd + " F" + str(speed) + "\n"    
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(5)
def cl_ab(axis1_angle, axis2_angle, axis3_angle, axis4_angle, axis5_angle, axis6_angle, speed = 1000):
#"""
#move robot motors to specified cartiesian coordinates linear endefector will fallow line

#if no motion is desired for a specific motor the function expects the value np.nan for that parameter
#"""
    cmd = "M20 G90 G0"
    if not np.isnan(axis1_angle):
        cmd = cmd + " x" + str(axis1_angle)
    if not np.isnan(axis2_angle):
        cmd = cmd + " Y" + str(axis2_angle)
    if not np.isnan(axis3_angle):
        cmd = cmd + " Z" + str(axis3_angle)
    if not np.isnan(axis4_angle):
        cmd = cmd + " A" + str(axis4_angle)
    if not np.isnan(axis5_angle):
        cmd = cmd + " B" + str(axis5_angle)
    if not np.isnan(axis6_angle):
        cmd = cmd + " C" + str(axis6_angle)    
    cmd = cmd + " F" + str(speed) + "\n"    
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1    
    time.sleep(5)
def cf_r(axis1_angle = 0, axis2_angle = 0,axis3_angle = 0, axis4_angle = 0, axis5_angle = 0, axis6_angle = 0, speed = 1000):
#"""
#cartiesian fast move relative to current position
#"""
    cmd = "M20 G91 G0 X" + str(axis1_angle) + " Y" + str(axis2_angle) + " Z" + str(axis3_angle) + " A" + str(axis4_angle) \
    + " B" + str(axis5_angle) + " C" + str(axis6_angle) + " F" + str(speed) + "\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(5)        
def cl_r(axis1_angle = 0, axis2_angle = 0,axis3_angle = 0, axis4_angle = 0, axis5_angle = 0, axis6_angle = 0, speed = 1000):
#"""
#cartiesian leniear move relative to current position
#"""
    cmd = "M20 G91 G1 X" + str(axis1_angle) + " Y" + str(axis2_angle) + " Z" + str(axis3_angle) + " A" + str(axis4_angle) \
    + " B" + str(axis5_angle) + " C" + str(axis6_angle) + " F" + str(speed) + "\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(5)
def homing_sync():
#"""
#return homing command all motors home simaltaiously 

#must be called after robot is reset to unlock motors
#"""
    cmd = "$h\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(20)

def homing_indiv():
#"""
#return homing command all motors move one at a time

#must be called after robot is reset to unlock motors
#"""
    cmd = "$hh\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(20)
def pump(on):
#"""
#returns comand to turn pump on or off
#"""
    if on:
        cmd = "M3S1000\n"
    else:
        cmd = "M3S0\n"
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1    
    time.sleep(0.5)
def grip(on):
#"""
#returns command to turn gripper on or off
#"""
    if on:
        cmd = "M4E65\n"
    else:
        cmd = "M4E40\n"    
    x = 0
    while(x < 1):
        f = open("input.txt","r+")
        ready = f.read(1)
        f.close()
        if ready == '^':
            f = open("input.txt","r+")
            f.write(cmd)
            f.close()
            x = 1
    time.sleep(0.5)        
def get_data():

#"""
#returns various data from mirobot as a tuple

#return values:
#0,     1,     2,       3,       4,          5,       6,       7,     8,
#error, state, a_angle, b_angle, c_angle,d_angle, x_angle, y_angle, z_angle,

#9,      10,     11,      12,      13,      14,      15,   16,   17
#x_cart, y_cart, z_cart, rx_cart, ry_cart, rz_cart, pump, grip, m_mode
#""" 
    df = open("response_mirobot.txt","r")
    data = df.readlines()
    df.close()
    length_output = len(data)
    current = length_output-1
    while(current >-1):
        if "<" in data[current]:
            data = data[current]

            target0 = data.find("<")
            target1 = data.find(",Angle(ABCDXYZ)")
            target2 = data.find(",Cartesian coordinate")
            target3 = data.find(",Pump")
            target4 = data.find(",Valve")
            target5 = data.find(",Motion_MODE")
            target6 = data.find(">")

            state = data[(target0 +1) : target1]
            angles = data[(target1 + 16) : target2]
            cart = data[(target2 + 34) : target3]
            pump = data[(target3 + 10) : target4]
            grip = data[(target4 + 11) : target5]
            m_mode = data[(target5 + 7) : target6]

            #isolate angle values
            a = 0
            b = -1
            c = -1
            d = -1
            x = -1
            y = -1
            z = -1

            a_end = -1
            b_end = -1
            c_end = -1
            d_end = -1
            x_end = -1
            y_end = -1
            z_end = len(angles) 

            fa = 0
            fb = 0
            fc = 0
            fd = 0
            fx = 0
            fy = 0

            for i in range(len(angles)):
                #A
                if angles[i]=="," and fa == 0:
                    a_end = i
                    fa = 1
                #B
                if i == a_end + 1 and a_end != -1:
                    b = i
                
                if b != -1 and angles[i]=="," and fb == 0:
                    b_end = i
                    fb = 1
                #C
                if i == b_end + 1 and b_end != -1:
                    c = i
                if c != -1 and angles[i]=="," and fc == 0:
                    c_end = i        
                    fc = 1
                #D
                if i == c_end + 1 and c_end != -1:
                    d = i
                if d != -1 and angles[i]=="," and fd == 0:
                    d_end = i    
                    fd = 1
                #X
                if i == d_end + 1 and d_end != -1:
                    x = i
                if x != -1 and angles[i]=="," and fx == 0:
                    x_end = i    
                    fx = 1
                #Y
                if i == x_end + 1 and x_end != -1:
                    y = i
                if y != -1 and angles[i] == "," and fy == 0:
                    y_end = i    
                    fy = 1
                #D
                if i == y_end + 1 and y_end != -1:
                    z = i
                    
            a_angle = angles[a: a_end]
            b_angle = angles[b: b_end]
            c_angle = angles[c: c_end]
            d_angle = angles[d: d_end]
            x_angle = angles[x: x_end]
            y_angle = angles[y: y_end]
            z_angle = angles[z: z_end]

            #isolate coordinate values
            x = 0
            y = -1
            z = -1
            rx = -1
            ry = -1
            rz = -1

            x_end = -1
            y_end = -1
            z_end = -1
            rx_end = -1
            ry_end = -1
            rz_end = len(cart)


            fx = 0
            fy = 0
            fz = 0
            frx = 0
            fry = 0
            frz = 0

            for i in range(len(cart)):
                #X
                if cart[i]=="," and fx == 0:
                    x_end = i
                    fx = 1
                #Y
                if i == x_end + 1 and x_end != -1:
                    y = i
                
                if y != -1 and cart[i]=="," and fy == 0:
                    y_end = i
                    fy = 1
                #Z
                if i == y_end + 1 and y_end != -1:
                    z = i
                if z != -1 and cart[i]=="," and fz == 0:
                    z_end = i        
                    fz = 1
                #Rx
                if i == z_end + 1 and z_end != -1:
                    rx = i
                if rx != -1 and cart[i]=="," and frx == 0:
                    rx_end = i    
                    frx = 1
                #Ry
                if i == rx_end + 1 and rx_end != -1:
                    ry = i
                if ry != -1 and cart[i]=="," and fry == 0:
                    ry_end = i    
                    fry = 1
                #Rz
                if i == ry_end + 1 and ry_end != -1:
                    rz = i
                if rz != -1 and cart[i] == "," and frz == 0:
                    rz_end = i    
                    frz = 1
                    
            x_cart = cart[x: x_end]
            y_cart = cart[y: y_end]
            z_cart = cart[z: z_end]
            rx_cart = cart[rx: rx_end]
            ry_cart = cart[ry: ry_end]
            rz_cart = cart[rz: rz_end]
            f = open("response_mirobot.txt", "r+")
            f.truncate()
            f.close()
            time.sleep(2)
            return 0, state, a_angle, b_angle, c_angle,d_angle, x_angle, y_angle, z_angle,\
            x_cart, y_cart, z_cart, rx_cart, ry_cart, rz_cart, pump, grip, m_mode 
            
        else:
            current = current - 1
            if current  < 1:
                time.sleep(2)
                return 1,
