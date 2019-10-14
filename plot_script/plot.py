import numpy as np
import matplotlib.pyplot as plt
import os
import sys


#file_name = "data/B_tests_up/4.dat"
file_name = sys.argv[1]
f = open(file_name,"r")

write_file_name = file_name[:-4]+"_short.dat"
write_file = open(write_file_name, "w+")

data = np.fromfile(f,dtype=np.float32)


#plt.plot(data)
#plt.ylim((-0.2,1.2))
#plt.show()

start = np.where(data>0.5)[0][0] - 10000

fig = plt.figure()
ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.2], xticklabels=[], ylim=(-.2, 1.2))
ax1 = fig.add_axes([0.1, 0.3, 0.8, 0.2], ylim=(-.2, 1.2))
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], ylim=(-.2, 1.2))
ax3 = fig.add_axes([0.1, 0.7, 0.8, 0.2], ylim=(-.2, 1.2))

# 2321800
# 472700

diff = 245000#2321800
tonext = 595000#472700
#start = 28435200
stop = start + diff

ax0.plot(data[start:stop]) 

start = stop + tonext
stop = start + diff

write_file.write(data[start:stop])

ax1.plot(data[start:stop])

start = stop + tonext
stop = start + diff


ax2.plot(data[start:stop])

start = stop + tonext
stop = start + diff

ax3.plot(data[start:stop])

if len(sys.argv) > 2:
    plt.show()


f.close()
write_file.close()
