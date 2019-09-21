import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def calcCks(input_msg):
    x = np.array(list(input_msg))
    x = x.astype(np.float)
    x[12:16] = [0, 0, 0, 0]
    chksm = np.zeros(4)
    for i in range(8):
        



input_msg = "10101011100011001000111101010110110011101001000011001100"

preamble = "0011001100110011001100110011001111"



def inv(a):
    if a == 1:
        return 0
    if a == 0:
        return 1


clk = 1
preamble = "".join([x*2 for x in preamble])
input_msg = "".join([x*2 for x in input_msg])
out_msg = ""
for bit in input_msg:
    #xor
    val = (int(bit)*inv(int(clk)))+(inv(int(bit))*int(clk))
    if val == 2:
        val = 0
    out_msg += str(val)
    clk = 1 - clk

out_msg = out_msg[0] + out_msg + "00"
msg = preamble + out_msg 
print(input_msg)
print(out_msg)
print(msg)

msg = "".join([x*1000 for x in msg])
plt.plot([ int (x) for x in msg ])
plt.ylim((-0.2,1.2))
plt.show()

