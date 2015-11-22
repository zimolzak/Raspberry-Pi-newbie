#!/usr/bin/env python

from blinkenlights import setup, cleanup, rhythm

pin = 18
tempo = 180 * 2
setup(pin)
for i in range(2):
    rhythm("1111010101011110", tempo, pin)
rhythm("1111001111001110", tempo, pin)
rhythm("1101101101111110", tempo, pin)
cleanup()
