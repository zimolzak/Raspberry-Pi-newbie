#!/usr/bin/env python

from blinkenlights import dimmer, setup, cleanup

pin = 18

setup(18)
dimmer(0.1, 4, 18)
cleanup()
