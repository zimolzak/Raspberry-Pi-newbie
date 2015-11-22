#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import light, clear
from time import sleep

pins = [32, 22, 18, 16]
#       blu grn red yel

for p in pins:
    setup(p)

for i in range(20):
    for p in [32, 22, 18, 16, 18, 22, 32]:
        clear(pins)
        light(p)
        sleep(0.07)
    clear(pins)
    sleep(0.5)

cleanup()
