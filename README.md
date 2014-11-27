The Hackable Clock
==================

A hackable alarm clock, made for experimentation to learn GPIO and programming.

Project page detailing out the hardware build is available at http://hackaday.io/project/3413-hack-ready-alarm-clock

Lessons and tutorials are coming soon.

Installation
------------

The hack-clock application is intended to be distributed as source, not in binary or packaged form, since
it is intended to be a teaching tool. Unfortunately this means we need to take a few extra steps to
install, but the entire process should take only a few minutes.

To install the hack-clock distribution:

1. Make sure your Raspberry Pi is up to date with the latest packages & firmware.
2. Enable I2C using raspi-config. It's listed under the advanced options.
3. Install WiringPi as described within http://wiringpi.com/download-and-install/
4. To let the pi user sense button presses, use the WiringPi GPIO Utility to permit non-root access to the pins. As an example: `sudo gpio export 17 out`
5. Ensure the pi user is added to the i2c group in /etc/group - there should be a line at the bottom of the file that looks like `i2c:x:110:pi`
6. Add the necessary Python tools using `sudo apt-get install python-distribute python-dev python-smbus i2c-tools`
7. Install the Pip dependency manager using `sudo easy_install pip`
8. Clone or download this repository. Different lessons are stored within branches of the repository.
9. Install hack-clock's dependencies using pip install -r requirements.txt
10. Copy the file `config.sample` to `config.py` and customize it for your environment (e.g. your local weather station)
11. Start the app by executing `./run_clock.py` from within the hack-clock directory

Bear in mind you may want to consider forking the source instead of cloning the parent repository -
that way you can make alterations and save your changes independently!

Starting the Clock at Boot
--------------------------

To start the clock as soon as your Raspberry Pi boots up:

1. Copy the startup script `hack-clock` into the directory `/etc/init.d`
2. Ensure the clock starts at boot using the command `sudo update-rc.d hack-clock defaults`
3. Start the clock with `sudo service hack-clock start`


License
=======

License is Apache Public License 2.0 (APL 2) unless otherwise noted.

The Adafruit libraries located in the /Adafruit directory are licensed separately, see Adafruit/README.md for details. 
The original code is available at https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

CodeMirror is licensed separately as detailed in views/codemirror/LICENSE. The CodeMirror codebase is
not directly committed into this repository (although it appears that way) - it is a subtree of
the repository available at https://github.com/codemirror/codemirror
