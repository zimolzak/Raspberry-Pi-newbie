"""Drive a cheesy 7-segment display made of LEDs."""

import RPi.GPIO as GPIO
from time import sleep
import sys

def light_segments(segstring, pins):
    assert type(segstring) == str
    for p in pins:
        GPIO.output(p, GPIO.LOW) # reset the many
    for c in segstring:
        GPIO.output(pins[int(c)], GPIO.HIGH)

alpha = dict(a='012345', b='13456', c='0146', d='23456', e='01346', f='0134',
             g='012356', h='14325', i='25', j='2564', k='134', l='146',
             m='02356', n='435', o='3456', p='01234', q='01235', r='34',
             s='01356', t='1436', u='14652', v='456', w='123456', x='35',
             y='12356', z='02346')

alpha[','] = '56'
alpha['.'] = '5'
alpha['"'] = '12'
alpha[';'] = '256'
alpha['-'] = '3'
alpha['_'] = '6'
alpha["'"] = '2'
alpha['!'] = '036'
alpha['?'] = '0234'
alpha[':'] = '36'
alpha['*'] = '036'
alpha['1'] = '25'
alpha['2'] = '02346'
alpha[')'] = '0256'
alpha['('] = '0146'
alpha['5'] = '01356'
alpha['4'] = '1235'
alpha['3'] = '02356'
alpha['6'] = '013456'
alpha['8'] = '0123456'
alpha['9'] = '012356'
alpha['7'] = '025'
alpha['0'] = '012456'

# not great: k   m  w  v x  z
#            |-  3  uu u 7  2

# FIXME - add the + character

def print_leds(string, pins, delay=2):
    assert type(string) == str
    try:
        for ch in string:
            c = ch.lower()
            if c in alpha.keys():
                light_segments(alpha[c], pins)
            else: # no lights for non-letters
                light_segments('', pins)
            sleep(delay)
    except KeyboardInterrupt:
        return
