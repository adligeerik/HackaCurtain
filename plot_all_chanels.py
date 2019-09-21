import numpy as np
import matplotlib.pyplot as plt
import os
import sys


folder = "data/"

fig = plt.figure()
ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.2], xticklabels=[], ylim=(-.2, 1.2))
ax1 = fig.add_axes([0.1, 0.3, 0.8, 0.2], ylim=(-.2, 1.2))
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], ylim=(-.2, 1.2))
ax3 = fig.add_axes([0.1, 0.7, 0.8, 0.2], ylim=(-.2, 1.2))


file_name = folder+"threshold_A_upp_short.dat"
f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
f.close()

fig.text(0.11,0.105,file_name)
ax0.plot(data[9500:]) 

file_name = folder+"threshold_A_down_short.dat"
f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
f.close()

fig.text(0.11,0.305,file_name)
ax1.plot(data[9500:])

file_name = folder+"threshold_B_upp_short.dat"
f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
f.close()

fig.text(0.11,0.505,file_name)
ax2.plot(data)

file_name = folder+"threshold_B_down_short.dat"
f = open(file_name,"r")
data = np.fromfile(f,dtype=np.float32)
f.close()

fig.text(0.11,0.705,file_name)
ax3.plot(data)



plt.show()