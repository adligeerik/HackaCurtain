import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def addCksum(input_msg):
    frame = ' '.join(input_msg[i:i+8] for i in range(0,len(input_msg),8)).split(' ')
    frame = [int(d, 2) for d in frame]
    frame[1] = frame[1] & 0xf0
    cksum = frame[0] ^ (frame[0] >> 4)

    for i in range(1,7):
        cksum = cksum ^ frame[i] ^ (frame[i]>>4)
       
    cksum = cksum & 0x0f 
    frame[1] = frame[1] | (cksum & 0x0f)
    
    return frame
    
def obfusicate(frame):
    for i in range(1, len(frame)):
        frame[i] = frame[i] ^ frame[i-1]
    return frame

def encode(argv):
    if len(argv) > 2:
        if argv[1] == "-h":
            input_msg = bin(int(argv[2], 16))[2:].zfill(8)
    else:
        input_msg = argv[1]

    preamble = "0011001100110011001100110011001111"

    frame = addCksum(input_msg)
    frame = obfusicate(frame)
    input_msg = "".join([ format(x, '#010b')[2:] for x in frame ])
    print(input_msg)

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
    print(msg)

    msg = "".join([x*1000 for x in msg])
    return msg