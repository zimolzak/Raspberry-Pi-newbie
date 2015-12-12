#!/usr/bin/env python

from blinkenlights import dimmer, setup, cleanup

pin = 18
bpm = 50

setup(pin)

up = range(10)
down = range(9)
down.reverse()
spectrum = up + down + [-1]

period = 60.0 / bpm # period is in seconds
time_per_level = period / len(spectrum)
# if time_per_level > 0.08 then the levels look too jerky.

for i in range(10): # 10 beats
    for j in (spectrum):
        brightness = (j+1) / 10.0
        dimmer(brightness, time_per_level, pin)

cleanup()
