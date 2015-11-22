import RPi.GPIO as GPIO

def light_only(pin, pinlist):
    for p in pinlist:
        GPIO.output(p, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
