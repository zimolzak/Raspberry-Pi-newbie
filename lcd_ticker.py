#!/usr/bin/env python

"""Display stock quotes on LCD"""

from ystockquote import get_price, get_change
from lcd import lcd_string, tn

symbols = ['AAPL', 'MSFT', 'F', 'T', 'KO', 'GOOG', 'SYK', 'DIS', 'GM', 'GE',
           'BAC', 'IBM', 'C', 'AMZN', 'AET', 'DOW', 'INTC', 'PFE', 'MRK', 'RTN']

while(True):
    for s in symbols:
        try:
            ticker_string = s + ' ' + get_price(s) + ' ' + get_change(s) + ' '
        except KeyboardInterrupt:
            break
        lcd_string(ticker_string, tn)
