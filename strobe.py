#!/usr/bin/env python

from blinkenlights import strobe, setup, cleanup

hertz = 10
duration = 10
pin = 18

setup(pin)
strobe(hertz, duration, pin)
cleanup()
