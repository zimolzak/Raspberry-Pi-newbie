#!/usr/bin/env python

"""Rhythm of 'YYZ' by Rush."""

from blinkenlights import letter, setup, cleanup

pin = 18
setup(pin)
for i in range(2):
    letter('-.--', pin)
    letter('-.--', pin)
    letter('--..', pin)
cleanup()
