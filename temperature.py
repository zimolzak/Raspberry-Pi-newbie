#!/usr/bin/env python

"""Get temperature sensor to work"""

# adapted from https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software

import glob
from time import sleep

period = 0.3333
duration = 8
samples = int(duration / float(period))
freq = 1.0 / period

series = []

print "inputting", samples, "samples,", "at", freq, "Hz"

####

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

lines = open(device_file, 'r').readlines()

t = int(lines[1][-6:])

print t

temp_c = t / 1000.0
temp_f = temp_c * 9.0 / 5.0 + 32.0
print temp_c, temp_f

quit()

####



for i in range(samples):
    series.append((GPIO.input(pin_sense)) ^ 1)
    print series[i]
    sleep(period)


