import numpy as np
import matplotlib.pyplot as plt
import os
import sys


#settings
pulse_width = 95000
window = 0
file_name = "threshold_short.dat"


f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
old_value = data[0]
decoded_data = np.zeros(64)
decoded_index = np.zeros(64)
pulse_high_counter = 0
pulse_low_counter = 0
dd_counter = 0

f_start = True
f_zero = False
f_one = False

i = 0
while True:
    if f_start:
        if data[i] > 0.99:    
            pulse_high_counter += 1
        elif data[i] != old_value and data[i] < 0.01:
            print("Falling edge at: " + str(i) + ", Pulse counter: " + str(pulse_high_counter))
            if pulse_high_counter >= pulse_width:
                f_start = False
                print("Thick pulse width: " + str(pulse_high_counter))
                print("Start pulse end at: " + str(i))
                i += pulse_width/4-window
            pulse_high_counter = 0
    else:
        #Rising edge
        if old_value < 0.01 and data[i] > 0.99:
            print("Rising edge at: " + str(i))
            decoded_data[dd_counter] = 1
            decoded_index[dd_counter] = i
            dd_counter += 1
            i += pulse_width/4-window
        
        #Falling edge
        elif old_value > 0.01 and data[i] < 0.99:
            print("Falling edge at: " + str(i))
            decoded_data[dd_counter] = 0
            decoded_index[dd_counter] = i
            dd_counter += 1
            i += pulse_width/4-window

    old_value = data[i]
    i += 1
    if i >= len(data):
        break
    #print(i)

fig = plt.figure()
ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.2], xticklabels=[], ylim=(-.2, 1.2))
ax0.plot(data[80000:])
ax0.plot(decoded_index, np.ones(64), '*')
plt.savefig('foo.png')

print("Decoded data: " + str(decoded_data))
            
    
    
