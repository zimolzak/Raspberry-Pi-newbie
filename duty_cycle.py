#!/usr/bin/env python

from blinkenlights import dimmer, setup, cleanup

pin = 18

setup(pin)

up = range(10)
down = range(9)
down.reverse()

for i in range(10):
    for j in (up + down):
        brightness = (j+1) / 10.0
        dimmer(brightness, 0.1, pin)

cleanup()
