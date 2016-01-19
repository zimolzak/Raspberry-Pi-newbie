#!/usr/bin/env python

"""Display stock quotes on LCD"""

import ystockquote as y
from lcd import lcd_string, tn

symbols = ['^IXIC', 'YMH16.CBT', 'YHOO', 'AAPL', 'MSFT', 'F', 'T', 'KO',
           'GOOG', 'SYK', 'DIS', 'GM',
           'GE', 'BAC', 'IBM', 'C', 'AMZN', 'AET', 'DOW', 'INTC', 'PFE',
           'MRK', 'RTN', 'BUD', 'LUV', 'K', 'V', 'X', 'BMY', 'JNJ', 'VRTX',
           'MCD', 'TCLRY', 'AFFX', 'TWTR', 'WMT', 'YUM', 'WFM']

def compact_quote(symbol):
    a = y.get_all(symbol)
    try:
        L52 = int(round(float(a['fifty_two_week_low']), 0))
    except ValueError:
        L52 = '_'
    try:
        P = round(float(a['price']), 1)
    except ValueError:
        P = '_'
    try:
        C = a['change']
    except ValueError:
        C = '_'
    try:
        H52 = int(round(float(a['fifty_two_week_high']), 0))
    except ValueError:
        H52 = '_'
    try:
        PE = round(float(a['price_earnings_ratio']), 1)
    except ValueError:
        PE = '_'
    try:
        Cp = int(round(float(C) / float(P) * 100))
    except ValueError:
        Cp = '_'
    return '{} {} {}% [{} {}] PE {}'.format(symbol, P, Cp, L52, H52, PE)[0:31]

while(True):
    try:
        for s in symbols:
            printme = compact_quote(s)
            print printme
            lcd_string(printme, tn, 15)
    except KeyboardInterrupt:
        break
