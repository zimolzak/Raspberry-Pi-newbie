#!/bin/sh

sudo killall wpa_supplicant

sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
