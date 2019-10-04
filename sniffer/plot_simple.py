import numpy as np
import matplotlib.pyplot as plt
import os
import sys


#file_name = "data/B_tests_up/4.dat"
file_name = sys.argv[1]
f = open(file_name,"r")

data = np.fromfile(f,dtype=np.float32)

plt.plot(data)
#plt.ylim((-0.2,1.2))
plt.show()

f.close()

