#!/usr/bin/env python
import ystockquote as y

x = 'SYK'
a = y.get_all(x)

L52 = int(round(float(a['fifty_two_week_low']), 0))
P = round(float(a['price']), 1)
C = a['change']
H52 = int(round(float(a['fifty_two_week_high']), 0))
PE = round(float(a['price_earnings_ratio']), 1)
Cp = int(round(float(C) / float(P) * 100))

printme = '{} {} {}% [{} {}] PE {}'.format(x, P, Cp, L52, H52, PE)

print printme
