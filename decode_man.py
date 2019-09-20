import numpy as np
import matplotlib.pyplot as plt
import os
import sys


#settings
pulse_width = 50000

old_value = data[0]
decoded_data = np.array(32)
pulse_counter = 0
dd_index = 0

f_start = True
f_zero = False
f_one = False


for value in data:
    if f_start:
        if value > 0:    
            pulse_counter += 1
        elif value != old_value: and value < 1:
            if pulse_counter >= pulse_width:
                pulse_counter = 0
                f_flag = False
    else:
        if old_value < 0.01 and value > 0.99:
            if pulse_counter > int(pulse_width/4.2):
                if not f_zero and not f_one:
                    #we have the first digit
                    decoded_data[dd_index] = 0
                    f_zero = True
                #Change between 1 and 0, and 0 to 1
                f_zero = not f_zero
                f_one = not f_one
                decoded_data[dd_index] = int(f_one)
            elif pulse_counter > int(pulse_width/8.2):
                if not f_zero and not f_one:
                    #we have the first digit
                    decoded_data[dd_index] = 1
                    f_one = True
                decoded_data[dd_index] = int(f_one)   
            pulse_counter = 0
        else:
            pulse_counter += 1
    old_value = value
            
    
    
