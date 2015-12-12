#!/usr/bin/env python

"""Just strobe at certain freq for certain time."""

from blinkenlights import strobe, setup, cleanup

hertz = 10
duration = 10
pin = 18

setup(pin)
strobe(hertz, duration, pin)
cleanup()
