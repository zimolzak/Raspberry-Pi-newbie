# Library of various functions for lighting LEDs.
# Adapted from code by Rahul Kar.
# http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html

import RPi.GPIO as GPIO
from time import sleep

def onoff(ontime, offtime, pin):
    """Base function that does the real work calling GPIO functions."""
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

dash_t = 0.2
pause_t = 0.1
dot_t = 0.1
letter_t = 0

def dash(pin):
    onoff(dash_t, pause_t, pin) # closure

def dot(pin):
    onoff(dot_t, pause_t, pin)

def letter(string, pin):
    """Input a string of .- and flash in Morse."""
    for char in string:
        if char == '-':
            dash(pin)
        if char == '.':
            dot(pin)
    sleep(letter_t)

def rhythm(spec, bpm, pin):
    """Input a string of 01 and flash at certain tempo."""
    sec_per_beat = 60.0 / bpm
    half_cycle = sec_per_beat / 2.0
    for char in spec:
        if char == "1":
            onoff(half_cycle, half_cycle, pin)
        if char == "0":
            sleep(sec_per_beat)

def dimmer(proportion, duration, pin):
    hertz = 60
    cycles = hertz * duration
    period = 1.0 / hertz
    on = proportion * period
    off = period - on
    for i in range(cycles):
        onoff(on, off, pin)
