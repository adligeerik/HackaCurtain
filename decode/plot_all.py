import numpy as np
import matplotlib.pyplot as plt
import os
import sys


f= open("threshold.dat","r")


data = np.fromfile(f,dtype=np.float32)


plt.plot(data)
plt.ylim((-0.2,1.2))
plt.show()


plt.show()


f.close()

