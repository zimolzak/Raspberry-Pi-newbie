#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import light, clear
from time import sleep
from random import randint

pins = [32, 22, 18, 16]
#       blu grn red yel

for p in pins:
    setup(p)

for i in range(20):
    k1 = randint(5, 10) * 0.01
    k2 = randint(5, 20) * 0.1
    for p in [32, 22, 18, 16, 18, 22, 32]:
        clear(pins)
        light(p)
        sleep(k1)
    clear(pins)
    sleep(k2)

cleanup()
