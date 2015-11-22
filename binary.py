#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import encode, light, clear
from time import sleep

all_leds = [32, 22, 18, 16]
#           blu grn red yel

for p in all_leds:
    setup(p)

clear(all_leds)
light(32)
sleep(1)
light(22)
sleep(2)
clear(all_leds)
sleep(1)
encode(3, all_leds)
sleep(2)
clear(all_leds)






for i in range(31):
    encode(i, all_leds)
    sleep(1)


cleanup()
