#!/bin/sh

modprobe i2c-dev # requires root
sudo -u pi LCDd -c /home/pi/Desktop/Raspberry-Pi-newbie/LCDd.conf
