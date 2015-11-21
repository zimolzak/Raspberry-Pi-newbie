#!/usr/bin/env python

# Adapted from code by Rahul Kar
# http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

import RPi.GPIO as GPIO
from time import sleep

hertz = 10
duration = 4

nflashes = hertz * duration
seconds_to_sleep = 1.0 / hertz / 2

GPIO.setmode(GPIO.BOARD) # means, like, wire 11, not GPIO 11
GPIO.setup(11, GPIO.OUT) # requires root?

def onoff(period):
    GPIO.output(11, GPIO.HIGH)
    sleep(period)
    GPIO.output(11, GPIO.LOW)
    sleep(period)

for i in range(nflashes):
    onoff(seconds_to_sleep)

GPIO.cleanup()
