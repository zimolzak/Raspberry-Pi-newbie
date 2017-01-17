#!/usr/bin/env python

"""Test Raspberry Pi camera!

Just rewrite the same filename again and again. Useful for pointing
the camera in the right direction, etc.
"""

import picamera
import sys
from time import sleep
from fractions import Fraction
import shutil

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = False # usually True
camera.rotation = 90
camera.resolution = (648, 486) #exactly quarter
camera.resolution = (432, 324) #exactly sixth

# shutter_speed analog_gain digital_gain exposure_mode awb_mode
# awb_gains iso framerate 

camera.framerate = Fraction(1, 6)
sec = 1
camera.shutter_speed = int(sec * 1000000)
camera.exposure_mode = 'off'
camera.iso = 800

try:
    while True:
        sleep(10)
        camera.capture("temp.jpg", quality=40)
        shutil.copy("temp.jpg", filename)
except KeyboardInterrupt:
    pass
