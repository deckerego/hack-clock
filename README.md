The Hackable Clock
==================

A hackable alarm clock, made for experimentation in order to build programming skills as well as the basics of circuit building.

Lessons and tutorials are currently a work-in-progress, however drafts are available at http://hackclock.deckerego.net/


Building the Hardware
---------------------

Step-by-step instructions for creating your clock are available at http://hackaday.io/project/3413-hack-ready-alarm-clock

A suggested list of hardware you might need to buy is saved as a wishlist at Adafruit: https://www.adafruit.com/wishlists/413935

Installation
------------

I'm assuming that you are starting with the Raspian Minimal Linux distribution. NOOBS or the like also works, but Raspian Minimal is small enough to fit on a 2GB microSD card. To install the hack-clock distribution on top of it:

1. Make sure your Raspberry Pi is up to date with the latest packages & firmware.
2. Enable I2C as described in Adafruit's tutorial at https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
3. Add the necessary Python and GStreamer dependencies using `sudo apt-get install wiringpi python-setuptools python-pip python-dev python-dateutil python-smbus gstreamer0.10-x gstreamer-tools gstreamer0.10-plugins-base gstreamer0.10-plugins-good gstreamer0.10-plugins-bad python-gst0.10`
4. Install hack-clock via `dpkg -i http://hackclock.deckerego.net/downloads/python-hackclock_2.0-beta-1_all.deb`
5. Install hack-clock's Python dependencies using `sudo pip install -r /usr/share/doc/hack-clock/requirements.txt`
6. Tweak `/etc/hack-clock.conf` and `/etc/default/hack-clock` to fit your needs (GPIO pins, correct weather station, etc.)
7. Start the app by executing `sudo service hack-clock start`


Usage
-----

Once the app starts, you should be able to get to the clock's web interface on port 9003. For example - http://192.168.1.2:9003/

Audio files and user-created source code is saved within the `/home/pi/hack-clock` directory - so it should be easily accessible for the pi user. This can be changed in `/etc/hack-clock.conf`.

Source is backed up each time the user saves - so if you accidentally screw something up it is quick to recover.

Clicking the "restore" button also opens up the source code for each lesson provided at http://hackclock.deckerego.net/. If you restore a lesson, you can find some good starting points and suggestions for your clock.


IN BETA - Coding With Blocks!
--------------------------

Python is currently the language of choice for teaching and customizing the clock, however a code-by-blocks editor (from Blockly, similar to Scratch) is currently going through a final round of testing and polish! If you would like to try it out early, change the following entry in `webapp/config.py`:

    'default_editor': '/blocks/edit'

If you would like to add a button that allows you to switch between Python and blocks editing, change the following in `webapp/config.py`:

    'disable_editor_button': False

Note that if you save a set of blocks, it will overwrite any Python coding you have performed. Likewise, if you make any Python edits it will overwrite whatever code was generated out of Blockly. You can still restore from previous Python or Blockly save points however.


Licenses
========

Unless otherwise noted, this software is released under the Apache Public License 2.0 (APL 2). A copy of this license is available within this distribution's base directory as the file `LICENSE`.

The Adafruit libraries located in the `/Adafruit` directory are licensed separately, see `runapp/Adafruit/README.md` for details.
The original code is available at https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

CodeMirror is licensed separately as detailed in `views/codemirror/LICENSE`. The CodeMirror codebase in this distribution is derived from the public repository available at https://github.com/codemirror/codemirror

Blockly is licensed separately as detailed in `views/blockly/LICENSE`. The Blockly codebase in this distribution is derived from the public repository available at https://github.com/google/blockly

Drawing of a 0.36" single digit seven-segment display has been released into the Public Domain by Inductiveload,
available at http://commons.wikimedia.org/wiki/File:7-Segment_Display,_0.36in,_Single_(shaded).svg
