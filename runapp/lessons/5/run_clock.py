#!/usr/bin/python

from datetime import datetime
from Libs.Clock import Clock
from Libs.SevenSegment import Display
from Libs.Input import Button
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

# Blink the display
def switchWeatherStations():
    # Clear the display
    display.setColon(False)
    display.setEvening(False)
    display.setHours(0)
    display.setMinutes(0)

    # Wait for about three seconds
    clock.waitAbout(3)

# What to do when you press a button
Button(24).whenPressed(switchWeatherStations)

# Show the current time
def showCurrentTime():
    now = datetime.now()

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
