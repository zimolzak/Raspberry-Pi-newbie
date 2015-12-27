#!/usr/bin/env python

"""Display standard input on LEDs."""

import sys
import RPi.GPIO as GPIO
from seven_segment import print_leds

pins = [17, 23, 24, 22, 27, 25, 5]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

pipe_contents = sys.stdin.read()

try:
    for c in pipe_contents:
        print_leds(c)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
