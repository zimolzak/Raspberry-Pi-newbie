#!/usr/bin/env python

"""Temperature into database"""

import glob
from time import sleep
import urllib2
import urllib

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

        data = {}
        data['temperature'] = str(temp_f)
        data['room'] = '1'
        url_values = urllib.urlencode(data)
        url = 'http://192.168.1.4/addtemperature'
        full_url = url + '?' + url_values
        data = urllib2.urlopen(full_url)
        print data.read()
        sleep(60)
except KeyboardInterrupt:
    pass
