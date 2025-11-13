The Hackable Clock
==================

A hackable alarm clock, made for experimentation in order to build programming skills as well as the basics of circuit building.

Lessons and tutorials are available at http://deckerego.github.io/hack-clock/


Project Status (Epilogue)
-------------------------

**This project was built on old versions of Raspian and Adafruit hardware, and will no longer work as-is.**

This project was intended to provide an easy-to-hack platform to teach coding and hardware basics. It received some great
early press, but the learning curve (and setup curve) was a bit steep for most kids. There was a lot of work that went into
the Hack Clock - and several are still running today!

As time has marched on so has the Raspberry Pi platform and the Adafruit hardware. The Adafruit audio bonnet made wiring up
audio so much easier, and the Pi Zero W was a fantastic low-profile platform. The 7-segment LED backpacks evolved, and
Raspbian drastically changed how Python and GPIO runs within the platform. Adafruit has also changed a lot of their
libraries, moving them to `pip` packages and leaning into managed Python environments.

All of this is great! However... it means that a major refactor of the Hack Clock would need to happen to get it to the
same level of functionality. Given the adoption level, if I _did_ bring back the Hack Clock it would need to be with a
complete rewrite.

I don't want to lose this code however - it was a remarkably stable platform that worked well. So this project will be archived,
and any future Hack Clock versions will be launched in a new repository.

Feel free to use this repository as inspiration, but note it will no longer run as-is. Still - I hope it can be a resource
to those looking for building teaching platforms!


Building the Hardware
---------------------

Step-by-step instructions for creating your clock are available at https://hackaday.io/project/3413/instructions

A suggested list of hardware you might need to buy is saved as a wishlist at Adafruit: https://www.adafruit.com/wishlists/413935


Usage
-----

Once the app starts, you should be able to get to the clock's web interface on port 9003. For example - http://raspberrypi:9003/

Audio files and user-created source code is saved within the `/home/pi/hack-clock` directory - so it should be easily accessible for the pi user. This can be changed in `/etc/hack-clock.conf`.

Source is backed up each time the user saves - so if you accidentally screw something up it is quick to recover.

Clicking the "restore" button also opens up the source code for each lesson provided at http://hackclock.deckerego.net/. If you restore a lesson, you can find some good starting points and suggestions for your clock.


Installation
============

I'm assuming that you are starting with the Raspian Minimal Linux distribution available at https://www.raspberrypi.org/downloads/raspbian/ or pre-installed by several distributors. NOOBS or the like also works, but Raspian Minimal is small enough to fit on a 2GB microSD card.

To install the hack-clock distribution on top of Raspian:

1. Make sure your Raspberry Pi is up to date with the latest packages & firmware with `sudo apt-get update; sudo apt-get dist-upgrade`
2. Enable I2C by executing `sudo raspi-config` as described in Adafruit's tutorial: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
3. Add the necessary Python and GStreamer dependencies using the command: `sudo apt-get install wiringpi ntp python-bottle python-requests python-oauth2client python-httplib2 python-setuptools python-pip python-dev python-dateutil python-smbus gstreamer0.10-x gstreamer0.10-alsa gstreamer-tools gstreamer0.10-plugins-base gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly python-gst0.10`
4. Install hack-clock via `wget https://github.com/deckerego/hack-clock/releases/download/2.3.1/python-hackclock_2.3.1-1_all.deb; sudo dpkg -i python-hackclock_2.3.1-1_all.deb`
5. Tweak `/etc/hack-clock.conf` and `/etc/default/hack-clock` to fit your needs (GPIO pins, correct weather station, etc.). A list of observed weather stations is available at http://forecast.weather.gov/stations.php
6. Reboot your Pi to re-load modules and start the IDE web server


Upgrading from 2.x
------------------

Upgrading from another 2.x release is pretty easy. Just execute `wget https://github.com/deckerego/hack-clock/releases/download/2.3.1/python-hackclock_2.3.1-1_all.deb; sudo dpkg -i python-hackclock_2.3.1-1_all.deb` and reboot your clock!


Upgrading from 1.0
------------------

Earlier versions of Hack Clock installed the entire application in the user's home directory, however
starting with version 2.0 we are only installing lessons, audio, and the current running
code in the home directory.

If you are upgrading from an earlier version of Hack Clock, first make sure you back up your
earlier installation by copying your current Hack Clock directory, as in:

    cp hack-clock hack-clock_old

After installation, copy the `blocks_clock.xml`, `run_clock.py`, and any audio files
over to the new `hack-clock` directory within your own home directory.

The older version of Hack Clock also used the headphone jack instead of the I2S interface.
If you would like to continue to use the headphone jack, modify `/boot/config.txt` by
commenting out the I2S interfaces and un-commenting the `audio=on` parameter. For example:

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on
    #dtoverlay=hifiberry-dac
    #dtoverlay=i2s-mmap

Once you have commented out the I2S settings as shown above, subsequent upgrades should
just skip the I2S changes so you don't need to keep re-commenting things out.

You will also need to remove the custom `/etc/asound.conf` configuration file on your Pi -
it does not need to be present if you are using the headphone jack.


Coding With Blocks!
===================

Coding by Blocks is now the default way of programming the Hack Clock! If you would like to revert back to Python, change the following entry in `webapp/config.py`:

    'default_editor': '/python/edit'

If you would like to add a button that allows you to switch between Python and blocks editing, change the following in `webapp/config.py`:

    'disable_editor_button': False

Note that if you save a set of blocks, it will overwrite any Python coding you have performed. Likewise, if you make any Python edits it will overwrite whatever code was generated out of Blockly. You can still restore from previous Python or Blockly save points however.


Known Issues
============

The Google Music API (gmusicapi) requires lxml, which often requires native compilation for ARM. Compiling
lxml can take over 500M of RAM, which some smaller Raspberry Pi's don't have. To work around this, you
can increase the swap file size of your Pi by editing `/etc/dphys-swapfile` and setting the swapfile
value to:

    CONF_SWAPSIZE=512

After setting this value, you can have them take effect by restarting swap:

    sudo service dphys-swapfile stop
    sudo service dphys-swapfile start

Bear in mind that swap is *slow*, so the build will likely take a while.


Licenses
========

Unless otherwise noted, this software is released under the Apache Public License 2.0 (APL 2). Copyright 2017 John T. Ellis. A copy of this license is available within this distribution's base directory as the file `LICENSE`.

The Adafruit libraries located in the `/Adafruit` directory are licensed separately, see `lib/hackclock/runapp/Adafruit/README.md` for details.
The original code is available at https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

CodeMirror is licensed separately as detailed in `srv/hackclock/views/codemirror/LICENSE`. The CodeMirror codebase in this distribution is derived from the public repository available at https://github.com/codemirror/codemirror

Blockly is licensed separately as detailed in `srv/hackclock/views/blockly/LICENSE`. The Blockly codebase in this distribution is derived from the public repository available at https://github.com/google/blockly

Drawing of a 0.36" single digit seven-segment display has been released into the Public Domain by Inductiveload,
available at http://commons.wikimedia.org/wiki/File:7-Segment_Display,_0.36in,_Single_(shaded).svg

Audio files are licensed separately as detailed in `home/pi/hack-clock/audio/README.md`. Where applicable, the original source for each file is listed within the README.md file.
