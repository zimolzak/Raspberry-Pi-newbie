#!/usr/bin/env python

"""Play a dumb arpeggio. I recommend 1k resistor. Who needs a DAC?"""

import RPi.GPIO as GPIO
from blinkenlights import strobe

pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

hertz = 440
dur = 0.2

def play(pitches, dur=0.2, base=440, pin=26):
    for p in pitches:
        assert type(p) == int
        strobe(base * 2.0 ** (int(p) / 12.0), dur, pin)

play(range(1,14))

GPIO.cleanup()
