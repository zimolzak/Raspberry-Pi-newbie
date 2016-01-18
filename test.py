#!/usr/bin/env python
import ystockquote as y

x = 'SYK'
a = y.get_all(x)

# 'fifty_two_week_low', 'fifty_day_moving_avg', 'price', 'price_book_ratio', 'volume', 'market_cap', 'dividend_yield', 'ebitda', 'change', 'dividend_per_share', 'stock_exchange', 'two_hundred_day_moving_avg', 'fifty_two_week_high', 'price_sales_ratio', 'price_earnings_growth_ratio', 'earnings_per_share', 'short_ratio', 'avg_daily_volume', 'price_earnings_ratio', 'book_value'

L52 = int(round(float(a['fifty_two_week_low']), 0))
P = round(float(a['price']), 1)
C = a['change']
H52 = int(round(float(a['fifty_two_week_high']), 0))
PE = round(float(a['price_earnings_ratio']), 1)
Cp = int(round(float(C) / float(P) * 100))
ran = round((float(P) - float(L52)) / (float(H52) - float(L52)) * 100)

#printme = '{} {} {} {}% [{} {}] {}% PE {}'.format(x, P, C, Cp, L52, H52, ran, PE)
printme = '{} {} {}% [{} {}] PE {}'.format(x, P, Cp, L52, H52, PE)

print printme
print "_" * 31
print len(printme)

# price(x)
# print y.get_change(x)
# print y.get_52_week_high(x)
# print y.get_52_week_low(x)
# print y.get_price_earnings_ratio(x)
