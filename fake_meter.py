#!/usr/bin/env python

"""Mimic a one-dimensional bar graph.

Control an arbitrary number of LEDs. Make them light up or turn off,
one at a time, starting at one end of the list. Randomly decide
whether to go up or down.
"""

import RPi.GPIO as GPIO
from time import sleep
from random import randint

pins = [5, 22, 27, 17, 12, 25, 23, 18]
#pins = [26, 6, 13, 22]
npins = len(pins)

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD
GPIO.setup(pins, GPIO.OUT) # requires root

def display(value):
    assert 0 <= value <= npins
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset them all
    for p in pins[:value]:
        GPIO.output(p, GPIO.HIGH) # turn on the few

x = 2

try:
    while(True):
        x = x + randint(-1,1)
        if x > npins:
            x = npins
        if x < 0:
            x = 0
        display(x)
        sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
