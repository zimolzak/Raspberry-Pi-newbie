#!/usr/bin/env python

# Adapted from code by Rahul Kar
# http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

from strobe import strobe

hertz = 10
duration = 4

strobe(hertz, duration, 11)
