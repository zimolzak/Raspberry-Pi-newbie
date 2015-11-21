Raspberry-Pi-newbie
========

I just got a Raspberry Pi for my birthday. How do I make it work and
do things?

Wiring
--------

1. Note to self. Inside my Pi box, the red stripe on ribbon connects
with the red stripe *toward* the corner. In other words, red stripe
toward the little power-on LED, or toward the edge with the DISPLAY
connector, away from the edge with the CAMERA connector. This was
mostly obvious but not 100%.

2. Canakit T connector pin 11 (labeled as "17" meaning GPIO 17) -->
long leg of LED --> Short leg of LED --> 220 ohm --> GND (canakit T,
pin 39)

Blink software
--------

Adapted from code by Rahul Kar

http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

Edit the code to decide what frequency blink and for how many seconds.

Usage: `sudo ./blinken.py`
