# HackaCurtain

This repo contains tools for listening and transmitting messages for the somfy curtains system. Smofy transmitts on 433.42Mhz and uses amplitude shift key for modulation (ASK/OOK), and encodes it with Manchester code.

## Hardware used
* HackRF One
* Homemade antennas

## Getting started
* Install gnu radio companion
```
apt install gnuradio
```
* Install osmocom (hackrf one)
```
git clone https://git.osmocom.org/gr-gsm
cd gr-gsm
mkdir build
cd build
cmake ..
mkdir $HOME/.grc_gnuradio/ $HOME/.gnuradio/
make
make install
ldconfig
```

**scope.grc**

Records on 433.42Mhz processes it with a threshold for high and low. Then saves it 

**decode_man.py**

Takes the recorded file and decodes the Manchestercoding, then de-obfuscation and check the checksum

**manchester_encoding.py**

Obfuscation the message calculates the checksum and encodes the message with Manchester and adds the preamble 

**synt_v2.grc**

Sends a message on 433.42Mhz



![Recorded message with decoded edges (stars)](https://github.com/adligeerik/HackaCurtain/blob/master/plots/edgefinder.png)

*Recorded message with decoded edges (stars)*

![Recorded message over time](https://github.com/adligeerik/HackaCurtain/blob/master/plots/timeeoifneionv.png)

*Recorded message over time*

![Comparison between different remotes, up/down](https://github.com/adligeerik/HackaCurtain/blob/master/plots/check_code_does_not_change.png)

*Comparison between different remotes, up/down*
