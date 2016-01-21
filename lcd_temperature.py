#!/usr/bin/env python

"""Just print temperature"""

import glob
from time import sleep
from lcd import lcd_string, tn

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

try:
    while True:
        lines = open(device_file, 'r').readlines()
        string = lines[1][-6:].replace('=', '') 
        t = int(string)
        temp_c = t / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        print temp_f
        lcd_string(str(temp_f), tn, 1)
        lcd_string("    " + str(temp_f), tn, 1)

#        sleep(1)
except KeyboardInterrupt:
    pass


