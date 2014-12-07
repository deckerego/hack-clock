#!/usr/bin/python

import time
import datetime
from Libs.Clock import Clock
from Libs.Display import Display
from Libs.Weather import Weather
from Libs.Input import Button
from Libs.GStreamer import Speaker
from config import configuration

# The weather station
station_name = configuration.get('weather_station')
weather_station = Weather(station_name)

# Connect to the internal machine clock
clock = Clock()

# Connect to the LED display
display = Display()

# Connect to the speaker
speaker = Speaker()


# Show the current weather
def switchWeatherStations():
    # Clear the display
    display.setColon(False)
    display.setEvening(False)
    display.setHours(0)
    display.setMinutes(0)

    # Show the current temperature
    current_temp = weather_station.getCurrentTemp()
    display.setMinutes(current_temp)

    # Wait for about three seconds
    clock.waitAbout(3)
    

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


# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(1)

# What to do when you press a button
Button(24).whenPressed(switchWeatherStations)

# What to do when the internal clock ticks
clock.onTick(showCurrentTime)
