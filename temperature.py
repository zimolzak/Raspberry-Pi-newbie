#!/usr/bin/env python

"""Get temperature sensor to work"""

# adapted from https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software

import glob
from time import sleep
import RPi.GPIO as GPIO

####

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

####

pins = [24, 23, 18]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

def light_only(x):
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset the many
    GPIO.output(x, GPIO.HIGH)

def represent(temperature):
    if temperature >= 85:
        light_only(18)
    elif 72 < temperature < 85:
        light_only(23)
    else:
        light_only(24)

try:
    while True:
        lines = open(device_file, 'r').readlines()
        t = int(lines[1][-6:])
        temp_c = t / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        represent(temp_f)
        sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
