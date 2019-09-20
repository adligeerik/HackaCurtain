import numpy as np
import matplotlib.pyplot as plt
import os
import sys


f= open("threshold.dat","r")


data = np.fromfile(f,dtype=np.float32)


#plt.plot(data)
#plt.ylim((-0.2,1.2))
#plt.show()

fig = plt.figure()
ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.2], xticklabels=[], ylim=(-.2, 1.2))
ax1 = fig.add_axes([0.1, 0.3, 0.8, 0.2], ylim=(-.2, 1.2))
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], ylim=(-.2, 1.2))
ax3 = fig.add_axes([0.1, 0.7, 0.8, 0.2], ylim=(-.2, 1.2))

# 2321800
# 472700

diff = 2321800
tonext = 472700
start = 28435200
stop = start + diff

ax0.plot(data[start:stop]) 

start = stop + tonext
stop = start + diff

ax1.plot(data[start:stop])

start = stop + tonext
stop = start + diff

ax2.plot(data[start:stop])

start = stop + tonext
stop = start + diff

ax3.plot(data[start:stop])

plt.show()


f.close()

