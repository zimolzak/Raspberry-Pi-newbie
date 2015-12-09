#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pin = 7
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin, GPIO.IN) # requires root

for i in range(24):
    z = GPIO.input(pin)
    if z:
        print "high"
    else:
        print "low"
    sleep(0.33)

GPIO.cleanup()
