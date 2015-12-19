#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
from random import randint

pins = [26, 6, 13, 22]
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

while(True):
    x = x + randint(-1,1)
    if x > npins:
        x = npins
    if x < 0:
        x = 0
    display(x)
    sleep(0.2)

GPIO.cleanup()
