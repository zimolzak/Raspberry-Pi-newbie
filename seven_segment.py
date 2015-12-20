#!/usr/bin/env python

"""Drive a cheesy 7-segment display made of LEDs."""

import RPi.GPIO as GPIO
from time import sleep
import sys

pins = [17, 23, 24, 22, 27, 25, 5]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

pipe_contents = sys.stdin.read()

def light_segments(segstring):
    assert type(segstring) == str
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset the many
    for c in segstring:
        GPIO.output(pins[int(c)], GPIO.HIGH)

alpha = dict(a='012345', b='13456', c='0146', d='23456', e='01346', f='0134',
             g='012356', h='14325', i='25',
             j='2564', k='6', l='146', m='6', n='435', o='3456', p='01234',
             q='01235', r='34',
             s='01356', t='1436', u='14652', v='456', w='6', x='6',
             y='12356', z='6')

# fixme: kmwxz

def display(character):
    assert type(character) == type(str())
    assert len(character) == 1
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset the many
    for bit in range(8): # turn on the few
        if (ord(character) >> bit) % 2:
            GPIO.output(pins[bit], GPIO.HIGH)

for c in 'abcde':
    light_segments(alpha[c])
    sleep(1)

try:
    for c in pipe_contents:
        c = c.lower()
        if c in alpha.keys():
            light_segments(alpha[c])
        else: # no lights for non-letters
            light_segments('')
        sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
