#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import light_only
from time import sleep

pins = [32, 22, 18, 16]
#       blu grn red yel

for p in pins:
    setup(p)

for p in pins:
    light_only(p, pins)
    sleep(0.5)

cleanup()
