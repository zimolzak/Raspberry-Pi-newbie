Raspberry Pi newbie
========

I just got a Raspberry Pi for my birthday. How do I make it work and
do things?

WiFi
--------

The default way that `wpa_supplicant` gets started is:

`/sbin/wpa_supplicant -s -B -P /var/run/wpa_supplicant.wlan0.pid -i wlan0 -D nl80211,wext -c /etc/wpa_supplicant/wpa_supplicant.conf`

Here is a good way to find out what is going on:

`sudo wpa_supplicant -c /etc/wpa_supplicant/wpa_supplicant.conf -iwlan0 -d`

`wpa_gui &` is helpful for clicking and watching and such.

Eventually when it worked, I just did:

`sudo wpa_supplicant -c /etc/wpa_supplicant/wpa_supplicant.conf -iwlan0 &`

Check out file `wpa_supplicant.conf` in this repo for the code that
worked. I am not sure whether `key_mgmt=WPA-PSK` ends up getting
auto-changed to something else for my particular network.


Wiring for blinkenlights
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

Hint: the band Rush likes Morse code, things in 10/4 time, and the
city of Toronto.

Usage: `sudo ./main.py`
