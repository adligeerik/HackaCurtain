import sys
import numpy as np
import matplotlib.pyplot as plt


fileName = sys.argv[1]

f = open(fileName,"r")
dataFile = np.fromfile(f,dtype=np.float32)

plotData = []

thMax = 55
thMin = 50

prev = 1.0
for data in dataFile:
    if data > thMax or ((prev >= 0.99) and (data > thMin)):
        plotData.append(1)
    elif data < thMin or ((prev <= 0.01) and (data < thMax)):
        plotData.append(0)
    prev = plotData[-1]



plt.subplot(311)

# equivalent but more general
if len(sys.argv) >= 3:
    ax1=plt.subplot(2, 1, 1)
    ax2=plt.subplot(2,1,2)
    ax2.set_ylim([-0.2, 1.2])
# add a subplot with no frame
    ax2.plot(plotData)
    ax1.plot(dataFile)

newName = fileName.replace("../sniffer/", "../threshold/")
print("Saving to file: " + newName)
saveFile = open(newName, "w+")
saveFile.write(np.float32(plotData))
saveFile.close()
if len(sys.argv) >= 3:
    plt.show()


        
