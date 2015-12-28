#!/usr/bin/env python

"""Test Raspberry Pi camera!"""

import picamera
import sys
from time import sleep

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True

try:
    while True:
        sleep(0.5)
        camera.capture(filename)
except KeyboardInterrupt:
    pass
