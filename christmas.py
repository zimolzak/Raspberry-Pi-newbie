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

try:
    abab(5, t0)
except KeyboardInterrupt:
    pass

cleanup()
