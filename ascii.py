#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import sys

pins = [5, 22, 27, 17, 12, 25, 23, 18]
pins.reverse()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

pipe_contents = sys.stdin.read()

def display(character):
    assert type(character) == type(str())
    assert len(character) == 1
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset the many
    for bit in range(8): # turn on the few
        if (ord(character) >> bit) % 2:
            GPIO.output(pins[bit], GPIO.HIGH)

for c in pipe_contents:
    display(c)
    sleep(1)

GPIO.cleanup()
