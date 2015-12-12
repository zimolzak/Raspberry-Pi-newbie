#!/usr/bin/env python

"""Count upwards in binary using four LEDs."""

from blinkenlights import setup, cleanup
from fourleds import encode, light, clear
from time import sleep

all_leds = [32, 22, 18, 16]
#           blu grn red yel

for p in all_leds:
    setup(p)

for i in range(31):
    encode(i, all_leds)
    sleep(1)

cleanup()
