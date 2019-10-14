import sys
import numpy as np
import matplotlib.pyplot as plt


fileName = sys.argv[1]

f = open(fileName,"r")
dataFile = np.fromfile(f,dtype=np.float32)

plotData = [0]

thMax = 1.4
thMin = 1.3

for data in dataFile:
    prev = plotData[0]
    if data > thMax or (prev == 1 and not data < thMin):
        plotData.append(1)

    else:
        plotData.append(0)


plt.subplot(311)

# equivalent but more general
if len(sys.argv) >= 2:
    ax1=plt.subplot(2, 1, 1)
    ax2=plt.subplot(2,1,2)
    ax2.set_ylim([-0.2, 1.2])
# add a subplot with no frame
    ax2.plot(plotData)
    ax1.plot(dataFile)

newName = fileName.replace("../sniffer/", "../threshold/")
saveFile = open(newName, "w+")
saveFile.write(np.float32(plotData))
saveFile.close()
if len(sys.argv) >= 3:
    plt.show()


        
