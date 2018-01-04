#!/usr/bin/env python

# usage example for webcam:
#    cd /var/www/
#    sudo ~pi/Desktop/Raspberry-Pi-newbie/repeating_camera.py ceiling.jpg &

"""Test Raspberry Pi camera!

Just rewrite the same filename again and again. Useful for pointing
the camera in the right direction, etc.
"""

import picamera
import sys
from time import sleep
from fractions import Fraction
import shutil
#import datetime as dt

filename = sys.argv[1]
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True 

# Usually hflip = True. But "hflip = False" gives the desired mirror
# effect if you're facing your camera and facing your browser aka
# laptop screen.

camera.rotation = 0 # 0 means ether/usb side is up.
camera.resolution = (648, 486) #exactly quarter
camera.resolution = (432, 324) #exactly sixth

# shutter_speed analog_gain digital_gain exposure_mode awb_mode
# awb_gains iso framerate 

#camera.framerate = Fraction(1, 6)  #default supposedly 30 fps
#sec =  1.0/8 # 0 implies automatic
#camera.shutter_speed = int(sec * 1000000) # it's in microseconds
#camera.exposure_mode = 'off'
#camera.iso = 800

#camera.annotate_background = picamera.Color('black')

try:
    while True:
        sleep(5)
#        s = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        camera.annotate_text = "duh"
        camera.capture("temp.jpg", quality=40)
        shutil.copy("temp.jpg", filename)
#        print s
except KeyboardInterrupt:
    pass
