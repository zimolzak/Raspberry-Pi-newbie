#!/usr/bin/env python

from blinkenlights import dimmer, setup, cleanup

pin = 18
bpm = 70

setup(pin)

up = range(10)
down = range(9)
down.reverse()
spectrum = up + down + [-1]

period = 60.0 / bpm # seconds
time_per_level = period / len(spectrum)

for i in range(10):
    for j in (spectrum):
        brightness = (j+1) / 10.0
        dimmer(brightness, time_per_level, pin)

cleanup()
