import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def addCksum(input_msg):
    frame = ' '.join(input_msg[i:i+8] for i in range(0,len(input_msg),8)).split(' ')
    print("input_msg: " + input_msg)
    frame = [int(d, 2) for d in frame]
    print("input_msg converted:", ' '.join([bin(lst) for lst in frame]))
    print("cksum frame: " + str(bin(frame[1])))
    frame[1] = frame[1] & 0xf0
    print("cksum frame: " + str(bin(frame[1])))
    cksum = frame[0] ^ (frame[0] >> 4)

    for i in range(1,7):
        print("Frame: " + bin(frame[i]))
        print("nibble 1: " + bin(frame[i] & 0x0f), "nibble 2: " + bin(frame[i]>>4))
        cksum = cksum ^ (frame[i]>>4)
        print("Checksum in loop: " + bin(cksum))
        cksum = cksum ^ frame[i]
        print("Checksum in loop: " + bin(cksum))
       
    #cksum = cksum ^ (frame[6] & 0x0f)
    print("Checksum: "  + bin(cksum))
    cksum = cksum & 0x0f 
    print("Checksum: "  + bin(cksum))
    frame[1] = frame[1] | (cksum & 0x0f)
    # frame = ''.join
    ans = "".join([ bin(x)[2:] for x in frame ])
    return ans
    
def obfusicate():
    for i in range(1, frame.size):
        frame[i] = frame[i] ^ frame[i-1]


#input_msg = "10101110111010101110100101100101111111011010001111111111"

input_msg = sys.argv[1]
preamble = "0011001100110011001100110011001111"

input_msg = addCksum(input_msg)

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
#print(input_msg)
#print(out_msg)
print(msg)

msg = "".join([x*1000 for x in msg])
# plt.plot([ int (x) for x in msg ])
# plt.ylim((-0.2,1.2))
# plt.show()

