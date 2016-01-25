#!/usr/bin/env python

"""Temperature from 3 probes"""

import glob
from time import sleep
import urllib2
import urllib

base_dir = '/sys/bus/w1/devices/'
folder_list = glob.glob(base_dir + '28*')
therm_list = []
for f in folder_list:
    therm_list.append( f + '/w1_slave')

def file2temp(x):
    lines = open(x, 'r').readlines()
    string = lines[1][lines[1].find('t=')+2:]
    t = int(string)
    temp_c = t / 1000.0
    return temp_c * 9.0 / 5.0 + 32.0

try:
    while True:
        for i, t in enumerate(therm_list):
            temp_f = file2temp(t)
            data = {}
            data['temperature'] = str(temp_f)
            data['room'] = str(i+2)
            url_values = urllib.urlencode(data)
            url = 'http://127.0.0.1/addtemperature'
            full_url = url + '?' + url_values
            data = urllib2.urlopen(full_url)
            print data.read()
        sleep(60)
except KeyboardInterrupt:
    pass
