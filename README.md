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

* Instal custom block 
```
cd gr-trigger/build
make ../
make
sudo make install
sudo ldconfig
```
## How to use
### "Hacking"
When the address is known run `hack_roll_code.py`, it will run through the rolling code with an interval specefied. Example with command 2 (up) address 985e5c and invervall of 50 for the rolling code:
```
python2 hack_roll_code.py -c 2 -a 985E5C -s 0000 -i 50
```
`hack_roll_code.py` calls `top_block_transmit.py` and generates a new test code every second and transmit it untill the next code is made. Depending on how large the rolling code is it will take between a few seconds upp till 15 minutes to "hack" a curtain.

### Sniffing
In the folder `sniffer/`, run `python top_block_sniffer.py`, it will listen on 433.42Mhz and save one second of samples when it is triggered. The script saves samples in the same folder with extension ".dat". To decode the samples run `./sniffer.sh 2> /dev/null`, the script calls the `decoder_man.py` and pipes the output from the python script in to "log.txt". In the log file the decoded messages will be displayed with as rolling code, address and command.

## Scripts

**scope.grc**

Records on 433.42Mhz processes it with a threshold for high and low. Then saves it 

**decode_man.py**

Takes the recorded file and decodes the Manchestercoding, then de-obfuscation and check the checksum

**manchester_encoding.py**

Obfuscation the message calculates the checksum and encodes the message with Manchester and adds the preamble 

**synt_v2.grc**

Sends a message on 433.42Mhz

## Results and plots

With this code we mananged to hack (our own) curtains to move up and down, we manage to control them from the ground about 100 meters away, and that with just a hackrf on and some (allot of) time :).

![Recorded message with decoded edges (stars)](https://github.com/adligeerik/HackaCurtain/blob/master/plots/edgefinder.png)

*Recorded message with decoded edges (stars)*

![Recorded message over time](https://github.com/adligeerik/HackaCurtain/blob/master/plots/timeeoifneionv.png)

*Recorded message over time*

![Comparison between different remotes, up/down](https://github.com/adligeerik/HackaCurtain/blob/master/plots/check_code_does_not_change.png)

*Comparison between different remotes, up/down*
