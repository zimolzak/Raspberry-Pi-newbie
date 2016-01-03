#!/usr/bin/env python

"""Test Raspberry Pi camera!"""

import picamera
import sys
from time import sleep

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.resolution = (1296, 972) #exactly half

try:
    while True:
        sleep(2)
        camera.capture(filename, quality=50)
except KeyboardInterrupt:
    pass
