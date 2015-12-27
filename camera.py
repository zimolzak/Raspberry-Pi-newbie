#!/usr/bin/env python

"""Test Raspberry Pi camera!"""

import picamera
import sys

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.brightness = 65
#camera.contrast = 20

# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
camera.exposure_compensation = 6
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
