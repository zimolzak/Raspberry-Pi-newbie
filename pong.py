#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import light, clear
from time import sleep
from random import randint

pins = [37, 33, 31, 29, 36, 32, 22, 18]
#       yp  ym  gp  gm  rp  rm  bp  bm

setup(pins)

for i in pins:
    light(i)
    sleep(1)
    clear(pins)

cleanup()
