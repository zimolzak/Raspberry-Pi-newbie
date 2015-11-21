import RPi.GPIO as GPIO
from time import sleep

def onoff(period, pin):
    """Symmetric square wave, equal time on/off"""
    half_cycle = period / 2.0
    GPIO.output(pin, GPIO.HIGH)
    sleep(half_cycle)
    GPIO.output(pin, GPIO.LOW)
    sleep(half_cycle)

def strobe(freq, dur, pin):
    nflashes = freq * dur
    seconds_to_sleep = 1.0 / freq

    # Use Raspberry-Pi board pin numbers. In other words, 11 means pin
    # number 11, not GPIO 11.
    GPIO.setmode(GPIO.BOARD) 

    GPIO.setup(pin, GPIO.OUT) # requires root?
    for i in range(nflashes):
        onoff(seconds_to_sleep, pin)
    GPIO.cleanup()
