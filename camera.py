#!/usr/bin/env python

"""Test Raspberry Pi camera!"""

import picamera
import sys
from fractions import Fraction
from time import sleep

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True

camera.framerate = Fraction(1, 6)
camera.shutter_speed = 4000000
#camera.exposure_mode = 'off'
camera.iso = 1600
print "sleep"
sleep(4)
print "go"

# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

camera.capture(filename)
