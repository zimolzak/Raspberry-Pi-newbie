#!/usr/bin/env python

"""Play a dumb arpeggio. I recommend 1k resistor. Who needs a DAC?"""

import RPi.GPIO as GPIO
from blinkenlights import strobe

pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

hertz = 440
dur = 0.333

strobe(hertz, dur, pin)
strobe(hertz * 1.25, dur, pin)
strobe(hertz * 1.5, dur, pin)
strobe(hertz * 2, dur, pin)
strobe(hertz * 1.5, dur, pin)
strobe(hertz * 1.25, dur, pin)
strobe(hertz, dur, pin)

GPIO.cleanup()
