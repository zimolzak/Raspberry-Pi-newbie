#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pins = [26, 6, 13, 22]

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
GPIO.setup(pins, GPIO.OUT) # requires root

for p in pins:
    GPIO.output(p, GPIO.LOW)

for p in pins:
    GPIO.output(p, GPIO.HIGH)
    sleep(1)

GPIO.cleanup()
