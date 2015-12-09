Raspberry Pi newbie
========

I just got a Raspberry Pi for my birthday. How do I make it work and
do things?


Running software to play with LEDs
--------

`sudo ./strobe.py`

`sudo ./rush.py`

`sudo ./malkmus.py`

`sudo ./main.py`

`sudo ./binary.py`

`sudo ./pong.py`

`sudo ./switch.py`


Wiring for blinkenlights
--------

1. Note to self. Inside my Pi box, the red stripe on ribbon connects
with the red stripe *toward* the corner. In other words, red stripe
toward the little power-on LED, or toward the edge with the DISPLAY
connector, away from the edge with the CAMERA connector. This was
mostly obvious but not 100%.

2. The basic scheme is as follows. Canakit T connector pin 11 (labeled
as "17" meaning GPIO 17) --> long leg of LED --> Short leg of LED -->
220 ohm --> GND (canakit T, pin 39)

3. Wiring multiple LEDs to the same common resistor & ground can cause
some of them not to light. I hypothesize unequal voltages of the GPIO
pins, and/or unequal internal resistances of the LEDs.

4. Pull up goes as follows: +3 --> 1k ohm --> GPIO. Also 1k ohm -->
switch --> GND.


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


Play with my other repos
--------

* `curl -O https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz`

* `sudo apt-get update`

* `sudo apt-get install python-dev`

* `sudo python setup.py build`

* `sudo python setup.py install`

* `python setup.py test`

* curl -O 'https://pypi.python.org/packages/source/g/gensafeprime/gensafeprime-1.5.tar.gz'

* etc



