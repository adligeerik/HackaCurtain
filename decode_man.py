import numpy as np
import matplotlib.pyplot as plt
import os
import sys

#settings
window = 0
file_name = sys.argv[1]

if len(sys.argv) > 2:
    verbose = sys.argv[2]
else:
    verbose = 0

def deObfusicate(frame):
    for i in range(len(frame)-1, 0, -1):
        frame[i] = frame[i] ^ frame[i-1]
    return frame

def checCksum(input_msg):
    cksum = frame[0] ^ (frame[0] >> 4)
    for i in range(1,7):
        cksum = cksum ^ (frame[i]>>4)
        cksum = cksum ^ frame[i]
       
    cksum = cksum & 0x0f 
    return cksum


f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
old_value = data[0]
decoded_data = np.zeros(56)
decoded_index = np.zeros(56)
pulse_high_counter = 0
pulse_low_counter = 0
dd_counter = 0

f_start = True
f_cal = True

i = 0
while True:
    if f_start:
        if f_cal and (old_value > 0.01 and data[i] < 0.99): 
            f_cal =  False
            pulse_width = int(pulse_high_counter*1.7)
            pulse_high_counter = 0
            if verbose:
                print("Thick pulse width: " + str(pulse_width))
        elif data[i] != old_value and data[i] < 0.01:
            if verbose:
                print("Falling edge at: " + str(i) + ", Pulse counter: " + str(pulse_high_counter))
            if pulse_high_counter >= pulse_width:
                f_start = False
                i += pulse_width/4-window
            pulse_high_counter = 0
        if data[i] > 0.99:    
            pulse_high_counter += 1
    else:
        #Rising edge
        if old_value < 0.01 and data[i] > 0.99:
            if verbose:
                print("Rising edge at: " + str(i))
            decoded_data[dd_counter] = 1
            decoded_index[dd_counter] = i
            dd_counter += 1
            i += pulse_width/4-window
        
        #Falling edge
        elif old_value > 0.01 and data[i] < 0.99:
            if verbose:
                print("Falling edge at: " + str(i))
            decoded_data[dd_counter] = 0
            decoded_index[dd_counter] = i
            dd_counter += 1
            i += pulse_width/4-window

    old_value = data[i]
    i += 1
    if i >= len(data):
        break

ans = "".join([ str (int(x)) for x in decoded_data ])
frame = ' '.join(ans[i:i+8] for i in range(0,len(ans),8)).split(' ')
frame = [int(d, 2) for d in frame]

frame = deObfusicate(frame)
cksum = checCksum(frame)

#if int(ans,2) != 0 and cksum != 0:
print(file_name)
print(ans)
print("Frame: "+''.join('0x{:02X} '.format(x) for x in frame))
print("    Key: 0x{:02X}".format((frame[0])))
print("    Control: 0x{:02X}".format((frame[1] >> 4) & 0x0f))
print("    Checksum: {}".format("ok" if cksum==0 else "error"))
print("    Address: "+''.join('{:02X} '.format(x) for x in frame[4:7]))
print("    Rolling Code: "+''.join('{:02X} '.format(x) for x in frame[2:4]))
print('')
            
    
    
