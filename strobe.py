# Adapted from code by Rahul Kar
# http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

import RPi.GPIO as GPIO
from time import sleep

def onoff(ontime, offtime, pin):
    GPIO.output(pin, GPIO.HIGH)
    sleep(ontime)
    GPIO.output(pin, GPIO.LOW)
    sleep(offtime)

def strobe(freq, dur, pin):
    nflashes = freq * dur
    period = 1.0 / freq

    # Use Raspberry-Pi board pin numbers. In other words, 11 means pin
    # number 11, not GPIO 11.
    GPIO.setmode(GPIO.BOARD) 

    GPIO.setup(pin, GPIO.OUT) # requires root?
    for i in range(nflashes):
        onoff(period/2.0, period/2.0, pin)
    GPIO.cleanup()
