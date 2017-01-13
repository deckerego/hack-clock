#!/usr/bin/python

from datetime import datetime
import random
from Libs.Clock import Clock
from Libs.SevenSegment import Display
from Libs.Weather import Weather
from Libs.Input import Button
from Libs.GStreamer import Speaker
from config import configuration

# Connect to the internal machine clock
clock = Clock()

# Connect to the LED display
display = Display()

# Connect to the speaker
speaker = Speaker()

# Awesome music
songs = ["TestTrack.ogg", "AmicusMeus.ogg"]

# Play some music
def playMusic():
    random.shuffle(songs)
    speaker.playList(songs)

# If music is playing, stop. Otherwise, play!
def playStopMusic():
    if speaker.isPlaying():
        speaker.stop()
    else:
    	playMusic()

# Don't wake us up on the weekend!
def wakeUp():
    if not datetime.now().weekday() in (5, 6):
        playMusic()

# Turn on the alarm at 07:05 every morning
clock.atTime(7, 5, wakeUp)

# What to do when you press a button
Button(24).whenPressed(playStopMusic)

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
