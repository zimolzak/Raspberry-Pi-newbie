#!/usr/bin/env python

from blinkenlights import letter, setup, cleanup

pin = 11
setup(pin)
for i in range(2):
    letter('-.--', pin)
    letter('-.--', pin)
    letter('--..', pin)
cleanup()