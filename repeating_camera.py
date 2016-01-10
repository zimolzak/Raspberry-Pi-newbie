#!/usr/bin/env python

"""Test Raspberry Pi camera!

Just rewrite the same filename again and again. Useful for pointing
the camera in the right direction, etc.
"""

import picamera
import sys
from time import sleep

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.rotation = 90
camera.resolution = (1296, 972) #exactly half

try:
    while True:
        sleep(2)
        camera.capture(filename, quality=50)
except KeyboardInterrupt:
    pass
