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

try:
    for i in range(4):
        encode(5, pins)
        sleep(0.4)
        encode(10, pins)
        sleep(0.4)
except KeyboardInterrupt:
    pass

cleanup()
