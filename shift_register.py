#!/usr/bin/python

"""http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2"""

# usage: python shift_register.py &

import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

DEVICE_ADDRESS = 0x20 #7 bit addr (will be L shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
while(1):
    for byte in range(0x00, 0xff + 1):
        bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, byte)
        time.sleep(30.0 / 256)

#Write an array of registers
# ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
# bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
