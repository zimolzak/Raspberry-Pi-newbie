#!/usr/bin/env python

"""Display stock quotes on LEDs."""

import RPi.GPIO as GPIO
from seven_segment import print_leds
from ystockquote import get_price, get_change

pins = [17, 23, 24, 22, 27, 25, 5]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

print_leds(' ', pins)

symbols = ['AAPL', 'MSFT', 'F', 'T', 'KO', 'GOOG', 'SYK']

for s in symbols:
    try:
        ticker_string = s + ' ' + get_price(s) + ' ' + get_change(s) + ' '
    except KeyboardInterrupt:
        break
    print_leds(ticker_string, pins, 1)

GPIO.cleanup()
