hack-clock
==========

A hackable alarm clock, made for experimentation to learn GPIO and programming.

Project page detailing out the hardware build is available at http://hackaday.io/project/3413-hack-ready-alarm-clock

Lessons and tutorials are coming soon.

Installation
------------

1. Make sure your Raspberry Pi is up to date with the latest packages & firmware.
2. Enable I2C using raspi-config. It's listed under the advanced options.
3. sudo apt-get install python-distribute python-dev
4. sudo easy_install pip
5. Clone this repository or download the .ZIP, which will include the clock controller and some admin configs/scripts
6. Install hack-clock's dependencies using pip install -r requirements.txt
7. Start the app using `sudo python ./run_clock.py`

I'm working on simplifying the installation process and getting rid of the sudo requirement.

License
=======

License is Apache Public License 2.0 (APL 2) unless otherwise noted. The Adafruit
libraries are licensed separately, see Adafruit/README.md for details.
