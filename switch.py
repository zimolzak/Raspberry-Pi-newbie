#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

pin_switch = 7
pin_led = 22
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin_switch, GPIO.IN) # requires root
GPIO.setup(pin_led, GPIO.OUT) # requires root
GPIO.output(pin_led, GPIO.LOW)

period = 0.33


series = []

for i in range(24):
    z = GPIO.input(pin_switch)
    if z:
        print "not pushed"
        series.append(0)
    else:
        print "pushed"
        series.append(1)
    sleep(period)

for v in series:
    if v:
        GPIO.output(pin_led, GPIO.HIGH)
    else:
        GPIO.output(pin_led, GPIO.LOW)
    sleep(period)

GPIO.cleanup()
