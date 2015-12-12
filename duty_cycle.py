#!/usr/bin/env python

from blinkenlights import onoff, setup, cleanup

hertz = 60
proportion = 0.1
duration = 4
pin = 18

cycles = hertz * duration
period = 1.0 / hertz
on = proportion * period
off = period - on

setup(pin)
for i in range(cycles):
    onoff(on, off, pin)
cleanup()
