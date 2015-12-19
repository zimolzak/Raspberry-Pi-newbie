#!/usr/bin/env python

"""Play Happy Birthday in the dumbest way possible.

I recommend a 1k-ohm resistor. Who needs a DAC?
"""

import RPi.GPIO as GPIO
from blinkenlights import strobe
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def play(pitches, dur=0.4, base=440, pin=26):
    for p in pitches:
        assert type(p) == int
        strobe(base * 2.0 ** (p / 12.0), dur, pin)

## a bb b c db d eb e f gb g  ab a  bb b  c
## 0 1  2 3 4  5  6 7 8  9 10 11 12 13 14 15
##        3    5    7 8    10    12 13    15
##       sol   la  ti do   re    mi fa    sol

play([3, 5, 3, 8, 7, 7])
#   hap bir da to yoou
play([3, 5, 3, 10, 8, 8])
#   hap bir da to  yoou
play([3, 15, 12, 8, 7, 5]) 
#    hap bir day de so one
play([13, 12, 8, 10, 8, 8]) 
#     hap bir day to yoou

GPIO.cleanup()
