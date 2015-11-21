#!/usr/bin/env python

from strobe import strobe, setup, cleanup, onoff
from time import sleep

pin = 11

dash_t = 0.7
pause_t = 0.15
dot_t = 0.2
letter_t = 0.5

def dash():
    onoff(dash_t, pause_t, pin) # closure

def dot():
    onoff(dot_t, pause_t, pin)

def letter(string):
    for char in string:
        if char == '-':
            dash()
        if char == '.':
            dot()
    sleep(letter_t)

setup(pin)

letter('...')
letter('---')
letter('...')

cleanup()
