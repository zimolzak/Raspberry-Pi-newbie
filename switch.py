#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pin_switch = 7
pin_led = 22
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin_switch, GPIO.IN) # requires root
GPIO.setup(pin_led, GPIO.OUT) # requires root
GPIO.output(pin_led, GPIO.LOW)

period = 0.05
duration = 8
samples = int(duration / float(period))

series = []

print "inputting"

for i in range(samples):
    series.append((GPIO.input(pin_switch)) ^ 1)
    sleep(period)

print "outputting"

for v in series:
    if v:
        GPIO.output(pin_led, GPIO.HIGH)
    else:
        GPIO.output(pin_led, GPIO.LOW)
    sleep(period)

GPIO.cleanup()
