#!/usr/bin/python

from datetime import datetime
from Libs.Clock import Clock
from Libs.SevenSegment import Display

# Connect to the internal machine clock
clock = Clock()

# Connect to the LED display
display = Display()

# Show the current time
def showCurrentTime():
    now = datetime.now()

    # Set the hours
    display.setHours(now.hour)

    # Set the indicator lights
    display.setColon(True)

    # Set the minutes
    display.setMinutes(now.minute)

# What to do when the internal clock ticks
clock.onTick(showCurrentTime)

# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(1)
