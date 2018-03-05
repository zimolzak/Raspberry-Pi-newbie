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
import datetime as dt

FILENAME = sys.argv[1]

def setup_cam():
    """Return a picamera object with reasonable mirroring, rotation,
    shutter, and exposure.
    """
    # Other camera properties:
    # shutter_speed analog_gain digital_gain exposure_mode awb_mode
    # awb_gains iso framerate
    # camera.annotate_background = picamera.Color('black')
    #
    # Usually hflip = True. But "hflip = False" gives the desired mirror
    # effect if you're facing your camera and facing your browser aka
    # laptop screen.
    #
    #camera.vflip = True
    #camera.hflip = True
    #camera.rotation = 180
    ## camera.framerate = Fraction(1, 6)
    #duration_sec = 1
    #duration_microsec = int(duration_sec * 1000000)
    #camera.shutter_speed = duration_microsec
    #camera.exposure_mode = 'auto' # camera.exposure_mode = 'off'
    #camera.iso = 800
    camera = picamera.PiCamera()
    camera.resolution = (432, 324) #exactly sixth. Full = 2592, 1944
    camera.start_preview()
    sleep(2)
    return camera

CAM = setup_cam()

stored = -1 # force an archive on 1st loop iteration.

try:
    while True:
        sleep(5)
#        s = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        CAM.annotate_text = "duh"
        CAM.capture("temp.jpg", quality=40)
        sleep(0.5)
        shutil.copy("temp.jpg", FILENAME)
        current = dt.datetime.now().hour
        if current > stored or (current == 0 and stored == 23):
            stored = current
            shutil.copy("temp.jpg", 'hour'+str(current)+'.jpg')

except KeyboardInterrupt:
    camera.close()
