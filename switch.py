#!/usr/bin/env python

"""Input the pattern/rhythm of user pressing a switch, and mimic that
with an LED."""

import RPi.GPIO as GPIO
from time import sleep

pin_switch = 12
pin_led = 21
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin_switch, GPIO.IN) # requires root
GPIO.setup(pin_led, GPIO.OUT) # requires root
GPIO.output(pin_led, GPIO.LOW)

period = 0.02
duration = 10
samples = int(duration / float(period))
freq = 1.0 / period

series = []

print "inputting", samples, "samples,", "at", freq, "Hz"

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
