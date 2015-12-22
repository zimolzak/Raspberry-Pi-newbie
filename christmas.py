#!/usr/bin/env python

"""Make some LEDs blink in pleasant, maybe Christmas-like patterns.

Created for Christmas, using rhythms/patterns that remind me of
jingling sleigh bells. Be sure to use red and green LEDs. If you use 4
LEDs, there are 64 basic pattern possibilities (2**4 LED * 2 patterns
* 2 tempi).
"""

from blinkenlights import setup, cleanup
from fourleds import light, clear, encode
from time import sleep
from random import randint

pins = [32, 22, 18, 16]
setup(pins)
t0 = 0.4 # Basic time unit for the rhythm
xmax = (2 ** len(pins)) - 1

def abab(x, t):
    assert type(x) == int
    assert 0 <= x <= xmax
    for i in range(4):
        encode(x, pins)
        sleep(t)
        encode(xmax - x, pins)
        sleep(t)

def aabb(x, t):
    assert type(x) == int
    assert 0 <= x <= xmax
    k = 0.7 # Defines how legato vs staccato
    for i in range(2):
        for j in range(2):
            encode(x, pins)
            sleep(t * k)
            clear(pins)
            sleep(t * (1-k))
        for j in range(2):
            encode(xmax - x, pins)
            sleep(t * k)
            clear(pins)
            sleep(t * (1-k))

try:
    while(True):
        time_factor = randint(1,2)
        if randint(0,1):
            abab(randint(0,xmax), t0 * time_factor)
        else:
            aabb(randint(0,xmax), t0 * time_factor)
except KeyboardInterrupt:
    pass

cleanup()
