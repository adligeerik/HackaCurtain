#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Oct 14 19:29:40 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import trigger
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.vec_length = vec_length = int(100e3)
        self.samp_rate = samp_rate = 2e6
        self.folder = folder = "/home/erik/Dev/mini-hackathon/HackaCurtain/data/test/"
        self.center_freq = center_freq = 433.3e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_2.win)
        self.trigger_trigger_ff_0_0 = trigger.trigger_ff(0.01, 1000)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(30, 0)
        self.osmosdr_source_0.set_if_gain(40, 0)
        self.osmosdr_source_0.set_bb_gain(30, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200e3, 10e4, firdes.WIN_HAMMING, 6.76))
        self.blocks_threshold_ff_0 = blocks.threshold_ff(1.33, 1.4, 0)
        self.blocks_tagged_file_sink_0_0 = blocks.tagged_file_sink(gr.sizeof_float*1, int(samp_rate))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((10000, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 1.0/10000, 40, 1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_burst_tagger_0_0 = blocks.burst_tagger(gr.sizeof_float)
        self.blocks_burst_tagger_0_0.set_true_tag('burst',True)
        self.blocks_burst_tagger_0_0.set_false_tag('burst',False)




        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_burst_tagger_0_0, 0), (self.blocks_tagged_file_sink_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_burst_tagger_0_0, 1))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_burst_tagger_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.trigger_trigger_ff_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.trigger_trigger_ff_0_0, 0), (self.blocks_float_to_short_0_0, 0))

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200e3, 10e4, firdes.WIN_HAMMING, 6.76))

    def get_folder(self):
        return self.folder

    def set_folder(self, folder):
        self.folder = folder

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
