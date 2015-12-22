#!/usr/bin/env python

"""Make four LEDs ascend and descend, at a pleasant variety of
rates."""

from blinkenlights import setup, cleanup
from fourleds import light, clear, encode
from time import sleep
from random import randint

pins = [32, 22, 18, 16]
#       blu grn red yel

setup(pins)

t0 = 0.4

def abab(x, t):
    assert type(x) == int
    xmax = (2 ** len(pins)) - 1
    assert 0 <= x <= xmax
    for i in range(4):
        encode(x, pins)
        sleep(t)
        encode(xmax - x, pins)
        sleep(t)

def aabb(x, t):
    assert type(x) == int
    xmax = (2 ** len(pins)) - 1
    assert 0 <= x <= xmax
    k = 0.7 # Defines how legato vs stacatto
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
    abab(5, t0)
    aabb(5, t0)
except KeyboardInterrupt:
    pass

cleanup()
