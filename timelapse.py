#!/usr/bin/env python

"""Take a photo every so often"""

# http://picamera.readthedocs.org/en/release-1.10/index.html

import picamera
import time

base_file_name = "puzzle"

camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
camera.resolution = (1296, 972) #exactly half

delay = 60 # seconds
minutes = 120
samples = int(minutes * 60.0 / delay)

for i in range(samples):
    time.sleep(delay)
    t_hr = ''.join(map(str,time.localtime()[3:4])).zfill(2)
    t_min = ''.join(map(str,time.localtime()[4:5])).zfill(2)
    t_sec = ''.join(map(str,time.localtime()[5:6])).zfill(2)
    filename = base_file_name + t_hr + t_min + t_sec + '.jpg'
    print filename
    camera.capture(filename, quality=50)
