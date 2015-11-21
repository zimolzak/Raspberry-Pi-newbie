# Adapted from code by Rahul Kar
# http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

import RPi.GPIO as GPIO
from time import sleep

def onoff(ontime, offtime, pin):
    GPIO.output(pin, GPIO.HIGH)
    sleep(ontime)
    GPIO.output(pin, GPIO.LOW)
    sleep(offtime)
    
def setup(pin):
    # Use Raspberry-Pi board pin numbers. In other words, 11 means pin
    # number 11, not GPIO 11.
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(pin, GPIO.OUT) # requires root?

def cleanup():
    GPIO.cleanup()

def strobe(freq, dur, pin):
    nflashes = int(freq * dur)
    period = 1.0 / freq
    for i in range(nflashes):
        onoff(period/2.0, period/2.0, pin)

dash_t = 0.7
pause_t = 0.15
dot_t = 0.2
letter_t = 0.5

def dash(pin):
    onoff(dash_t, pause_t, pin) # closure

def dot(pin):
    onoff(dot_t, pause_t, pin)

def letter(string, pin):
    for char in string:
        if char == '-':
            dash(pin)
        if char == '.':
            dot(pin)
    sleep(letter_t)
