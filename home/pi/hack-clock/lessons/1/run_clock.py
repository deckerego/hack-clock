#!/usr/bin/python

from hackclock.runapp.Libs.Clock import Clock
from hackclock.runapp.Libs.SevenSegment import Display

# Connect to the internal machine clock
clock = Clock()

# Connect to the LED display
display = Display()

# Set the indicator lights
display.setColon(True)
display.setEvening(False)

# Set the hours
display.setHours(0)

# Set the minutes
display.setMinutes(0)

# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(1)
