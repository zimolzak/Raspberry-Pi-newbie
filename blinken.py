#!/usr/bin/env python

from strobe import strobe, setup, cleanup, onoff

hertz = 0.5
duration = 10
pin = 11

setup(pin)
strobe(hertz, duration, pin)
cleanup()
