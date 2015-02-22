#!/usr/bin/python

import time
import datetime
from Libs.Clock import Clock
from Libs.SevenSegment import Display
from Libs.GStreamer import Speaker

# Connect to the internal machine clock
clock = Clock()

# Connect to the LED display
display = Display()

# Connect to the speaker
speaker = Speaker()

# Play some music
def playMusic():
    speaker.playList(["TestTrack.ogg", "AmicusMeus.ogg"])

# Wake us up at 8:30 in the morning
clock.atTime(8, 30, playMusic)

# Show the current time
def showCurrentTime():
    now = datetime.datetime.now()

    # Set the hours
    is_evening = now.hour > 12
    display.setHours(now.hour if not is_evening else now.hour - 12)

    # Set the indicator lights
    display.setColon(True)
    display.setEvening(is_evening)

    # Set the minutes
    display.setMinutes(now.minute)

# What to do when the internal clock ticks
clock.onTick(showCurrentTime)

# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(1)
