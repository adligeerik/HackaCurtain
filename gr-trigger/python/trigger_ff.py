#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 


import numpy
from gnuradio import gr
#import Triggerclass

class trigger_ff(gr.sync_block):
    """
    docstring for block trigger_ff
    """
    def __init__(self, threshold, length):
        self.threshold = threshold
        self.triggered = 0
        self.length = length
        self.index = 0
        gr.sync_block.__init__(self,
            name="trigger_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        if in0 > self.threshold:
            self.triggered = 1

        if self.triggered:
            self.index += 1
            

        if self.index >= self.length:
            self.triggered = 0
            self.index = 0

        # out[:] = self.triggered
        out[:] = in0
        return len(output_items[0])

