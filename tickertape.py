#!/usr/bin/env python

"""Display stock quotes on LEDs."""

import RPi.GPIO as GPIO
from seven_segment import print_leds
from ystockquote import get_price, get_change

pins = [17, 23, 24, 22, 27, 25, 5] ## FIXME - annoying and bad, in 2 places
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

symbols = ['AAPL', 'MSFT', 'F', 'T', 'KO', 'GOOG', 'SYK']

ticker_string = ' '.join(symbols)

print ticker_string

# try:
#     for c in ticker_string:
#         print_leds(c)
# except KeyboardInterrupt:
#     pass

GPIO.cleanup()
