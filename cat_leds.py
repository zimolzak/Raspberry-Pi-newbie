#!/usr/bin/env python

"""Display standard input on LEDs."""

import sys
import RPi.GPIO as GPIO
from seven_segment import print_leds


pins = [6, 19, 5, 13, 20, 12, 16]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

pipe_contents = sys.stdin.read()

print_leds(pipe_contents, pins, 1/2.0)

GPIO.cleanup()
