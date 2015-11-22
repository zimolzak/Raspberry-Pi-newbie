import RPi.GPIO as GPIO

def light(pin):
    GPIO.output(pin, GPIO.HIGH)

def clear(pinlist):
    for p in pinlist:
        GPIO.output(p, GPIO.LOW)
    
