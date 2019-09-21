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

print(file_name + "\t" + ans)

# fig = plt.figure()
# ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.2], xticklabels=[], ylim=(-.2, 1.2))
# ax0.plot(data)
# ax0.plot(decoded_index, np.ones(56), '*')
# plt.show()


            
    
    
