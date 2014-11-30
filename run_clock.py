#!/usr/bin/python

import time
import datetime
from ClockDisplay import ClockDisplay
from Weather import Weather
from Input import Button
from config import configuration

# Connect to the LED display
display = ClockDisplay()

# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(1)

# The weather station
station_name = configuration.get('weather_station')
weather_station = Weather(station_name)

# What to do when a button is pressed
def switchWeatherStations():
    # Clear the display
    display.showTime = False
    display.setColon(False)
    display.setHours(0)

    # Show the current temperature
    current_temp = weather_station.getCurrentTemp()
    display.setMinutes(current_temp)

    # Wait three seconds
    time.sleep(3)
    display.showTime = True

# A button to press!
button = Button(24)
button.whenPressed(switchWeatherStations)

# Keep updating, never stop
while(True):
    if display.showTime:
        now = datetime.datetime.now()

        # Set the hours
        is_evening = now.hour > 12
        display.setHours(now.hour if not is_evening else now.hour - 12)

        # Set the indicator lights
        display.setColon(True)
        display.setEvening(is_evening)

        # Set the minutes
        display.setMinutes(now.minute)

        # Wait one second
        time.sleep(1)
