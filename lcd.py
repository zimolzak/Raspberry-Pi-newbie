#!/usr/bin/env python

from telnetlib import Telnet
import time
import sys

tn = Telnet('127.0.0.1', 13666, None)
pipe_contents = sys.stdin.read()
pipe_contents = pipe_contents.replace('\n', ' ')

tn.write("hello\n")
tn.write("screen_add s1\n")
tn.write("screen_set s1 -priority 1\n")
tn.write("widget_add s1 w1 string\n")
tn.write("widget_add s1 w2 string\n")

def lcd_string(x, telnet_obj, delay=2):
    L = []
    for i in range(len(x)):
        if i % (15+16) == 0:
            L.append(x[i:i+15+16])
    for s in L:
        s1 = s[0:15]
        s2 = s[15:]
        telnet_obj.write("widget_set s1 w1 1 1 {" + s1 + "}\n")
        telnet_obj.write("widget_set s1 w2 1 2 {" + s2 + "}\n")
        time.sleep(delay)

lcd_string(pipe_contents, tn)
