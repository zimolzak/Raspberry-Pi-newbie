#!/usr/bin/env python

from lcd import lcd_string, tn

while(True):
    s = raw_input(">")
    lcd_string(s, tn, 0)
