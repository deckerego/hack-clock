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
3. Ensure the pi user is added to the i2c group in /etc/group - there should be a line at the bottom of the file that looks like `i2c:x:110:pi`
4. sudo apt-get install python-distribute python-dev
5. sudo easy_install pip
6. Clone this repository or download the .ZIP, which will include the clock controller and some admin configs/scripts
7. Install hack-clock's dependencies using pip install -r requirements.txt
8. Copy the startup script `hack-clock` into the directory `/etc/init.d`
9. Ensure the clock starts at boot using the command `sudo update-rc.d hack-clock defaults`
10. Start the app using `sudo service hack-clock start`

Bear in mind you may want to consider forking the source instead of cloning the parent repository -
that way you can make alterations and save your changes independently!

License
=======

License is Apache Public License 2.0 (APL 2) unless otherwise noted. The Adafruit
libraries are licensed separately, see Adafruit/README.md for details.
