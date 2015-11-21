#!/usr/bin/env python

from strobe import strobe, setup, cleanup, onoff

pin = 11

dash = 0.7
pause = 0.15
dot = 0.2

setup(pin)

onoff(dot, pause, pin)
onoff(dot, pause, pin)
onoff(dot, pause + 0.5, pin)

onoff(dash, pause, pin)
onoff(dash, pause, pin)
onoff(dash, pause + 0.5, pin)

onoff(dot, pause, pin)
onoff(dot, pause, pin)
onoff(dot, pause + 0.5, pin)

cleanup()
