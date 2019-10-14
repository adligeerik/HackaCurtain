import sys
import numpy as np
import matplotlib.pyplot as plt

#preamble = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
preamble = [-1, -1, -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1]

fileName = sys.argv[1]

f = open(fileName,"r")
dataFile = np.fromfile(f,dtype=np.float32)

plotData = [0]

thMax = 0.04
thMin = -0.01

for data in dataFile:
    prev = plotData[-1]
    if data > thMax or (prev == 1 and not data < thMin):
        plotData.append(1)

    #if data < thMin or prev == 0:
    else:
        plotData.append(-1)



plt.subplot(311)

# equivalent but more general
ax1=plt.subplot(3, 1, 1)
ax1.set_ylim([-0.2, 1.2])

# add a subplot with no frame
ax2=plt.subplot(3,1,2)

startData = 78300
stopData = 79600
#ax1.plot(plotData[startData:stopData])
ax1.plot(plotData)
#ax1.ylim((-0.2,1.2))
#ax2.plot(dataFile[startData:stopData])
ax2.plot(dataFile)
preamble = plotData[69700:69800]
#print(preamble)
conv = np.convolve(plotData, preamble)
ax3=plt.subplot(3,1,3)
ax3.plot(conv)

plt.show()

        
