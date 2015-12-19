#!/usr/bin/env python

"""Play Happy Birthday in the dumbest way possible.

I recommend a 1k-ohm resistor. Who needs a DAC?
"""

import RPi.GPIO as GPIO
from blinkenlights import strobe

pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

hertz = 440
dur = 0.2

def play(pitches, dur=0.1, base=440, pin=26):
    for p in pitches:
        assert type(p) == int
        strobe(base * 2.0 ** (p / 12.0), dur, pin)

## a bb b c db d eb e f gb g  ab a  bb b  c
## 0 1  2 3 4  5  6 7 8  9 10 11 12 13 14 15

play([3,3,3,3,5,5,5,5,3,3,3,3,8,8,8,8,7,7,7,7,7,7,7,7]) # happy birthday to you
play([3,3,3,3,5,5,5,5,3,3,3,3,10,10,10,10,8,8,8,8,8,8,8,8]) # happy birthday to you
play([3,3,3,3,15,15,15,15,12,12,12,12,8,8,8,8,7,7,7,7,5,5,5,5]) 
#     happy   birth       day         dear    some    one
play([13,13,13,13,12,12,12,12,8,8,8,8,10,10,10,10,8,8,8,8,8,8,8,8]) 

GPIO.cleanup()
