#!/usr/bin/env python

from strobe import letter, setup, cleanup
from time import sleep

pin = 11

setup(pin)

letter('-.--', pin)
letter('-.--', pin)
letter('--..', pin)

cleanup()
