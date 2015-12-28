#!/usr/bin/env python

"""Take a photo every so often"""

# http://picamera.readthedocs.org/en/release-1.10/index.html

import picamera
import time

base_file_name = "dad"

camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True

delay = 1
minutes = 10 / 60.0
samples = int(minutes * 60.0 / delay)

for i in range(samples):
    time.sleep(delay)
    t_min = ''.join(map(str,time.localtime()[4:5])).zfill(2)
    t_sec = ''.join(map(str,time.localtime()[5:6])).zfill(2)
    filename = base_file_name + t_min + t_sec + '.jpg'
    camera.capture(filename)
    print filename
