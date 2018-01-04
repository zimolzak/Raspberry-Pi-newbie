Raspberry Pi newbie
========

I just got a Raspberry Pi for my birthday. How do I make it work and
do things?

Nice daemons to start after boot
--------
* sudo ~pi/Desktop/Raspberry-Pi-newbie/repeating_camera.py ceiling.jpg &

* python3 check_wifi.py &

* cd ../Mulder-quote-generator; python -u bot.py > log.txt &; mess w pid.txt

* cd ../sysadmin-webapp; nohup ./webapp.py &


Achievements unlocked
--------

In the category of pure blinkenlight demos:

* Represent STDIN on LEDs, as either ASCII binary or on a
  seven-segment display. We use the text of _Pride and Prejudice._
  Example: `cat pride_and_prejudice.txt | sudo ./cat_leds.py &`
* Count off the seconds in binary using LEDs.
* Fade an LED in/out by varying the duty cycle.
* Randomly varying LED bar graph meter.
* Raspberry Pi plays pong with itself using LEDs.
* Blink a single LED in rhythm of some programmed songs.
* Make a strobe light LED.
* Make a line of LEDs scan back and forth at random rates.

In the category of multimedia:

* Use an LED as a light sensor.
* Make musical square wave beeps on an old headphone that I cut up,
  without using a digital-analog converter .
* Record the rhythm of switch presses and play the rhythm back on an
  LED.
* Low light camera photos
* Temperature sensor controls LEDs.
* Time lapse photography
* Motion detection triggered camera
* Drive an LCD. `cat pride_and_prejudice.txt | ./lcd.py`
* Stock quotes to LCD
* Multiple temperature sensors to SQLite database & analytics

*Note:* to run, many of these require `sudo ./pong.py` or
equivalent. Ones that don't require sudo would include `ascii.py` and
`seven_segment.py`, which require STDIN piped input. See above.


Example temperature graphs
--------
![Graph of 3 temperature probes over time](https://dl.dropboxusercontent.com/u/38640281/github_img/threeTempVsTime.png)

![Rather nice plot of temperature 1 vs temperature 2](https://dl.dropboxusercontent.com/u/38640281/github_img/catbedVsRadiator.png)


Wiring
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

5. Temp sensor: 
    * red --> 3V3
    * black --> GND
    * yellow --> GPIO 4
    * red --> 1k ohm --> yellow
    * Add `dtoverlay=w1-gpio-pullup,gpiopin=4` to /boot/config.txt
    * sudo modprobe w1-gpio; sudo modprobe w1-therm

Shift register directly
--------
* sudo modprobe i2c-dev
* i2cdetect 1
* sudo apt-get install python-smbus



LCD
--------
* `dtparam=i2c_arm=on` to /boot/config.txt
* sudo modprobe i2c-dev
* sudo apt-get install i2c-tools
* i2cdetect 1
* sudo apt-get install lcdproc
* LCDd -c LCDd.conf &
* lcdproc -f -c lcdproc.conf

WiFi
--------

**TL;DR:** wpa_supplicant.conf is rather hellish.



The default way that `wpa_supplicant` gets started is:
`/sbin/wpa_supplicant -s -B -P /var/run/wpa_supplicant.wlan0.pid -i
wlan0 -D nl80211,wext -c /etc/wpa_supplicant/wpa_supplicant.conf`

Here is a good way to watch what is going on: `sudo wpa_supplicant
-c /etc/wpa_supplicant/wpa_supplicant.conf -iwlan0 -d`

`wpa_gui &` is helpful for clicking and watching and such.

Also consider `watch tail -n 15 /var/log/syslog`

Eventually when it worked [but merely manually], I just did: `sudo
wpa_supplicant -c /etc/wpa_supplicant/wpa_supplicant.conf -iwlan0 &`

Check out file `wpa_supplicant.conf` in this repo for the code that
worked. I think `key_mgmt=WPA-PSK` ends up getting auto-changed to
CCMP or something, on my particular network.

To get it to work **finally** automatically on reboot, the issue was
ap_scan=2 incompatibility with nl80211. Leaving off the forcing of
nl80211 driver from the command line would work, but clearly that
required manually starting wpa_supplicant, as it runs it "the default
way" (see above) on reboot. So basically I had to read
http://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf
which is different from my
/usr/share/doc/wpa_supplicant/examples/wpa_supplicant.conf.gz file!!
Key quote:

    # Note: ap_scan=2 should not be used with the nl80211 driver interface (the
    # current Linux interface). ap_scan=1 is optimized work working with nl80211.
    # For finding networks using hidden SSID, scan_ssid=1 in the network block can
    # be used with nl80211.


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
