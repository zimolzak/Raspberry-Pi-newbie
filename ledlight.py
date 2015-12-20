#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pin_switch = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_switch, GPIO.IN)

period = 0.25
duration = 30
samples = int(duration / float(period))
freq = 1.0 / period

series = []

print "inputting", samples, "samples,", "at", freq, "Hz"

for i in range(samples):
    print (GPIO.input(pin_switch)) ^ 1
    sleep(period)

print

GPIO.cleanup()
