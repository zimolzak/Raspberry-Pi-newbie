#!/usr/bin/env python

from strobe import letter, setup, cleanup
from time import sleep

pin = 11

setup(pin)

for i in range(2):
    letter('-.--', pin)
    letter('-.--', pin)
    letter('--..', pin)

cleanup()
