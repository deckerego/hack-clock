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

# Set the colon in the middle
display.setColon(True)

# The weather station
station_name = configuration.get('weather_station')
weather_station = Weather(station_name)

# What to do when a button is pressed
def switchWeatherStations(pinNumber):
  print "Button %d" % pinNumber

# A button to press!
button = Button(17)
button.whenPressed(switchWeatherStations)

# Keep updating, never stop
while(True):
  now = datetime.datetime.now()

  is_evening = now.hour > 12
  display.setHours(now.hour if not is_evening else now.hour - 12)
  display.setEvening(is_evening)

  display.setMinutes(now.minute)

  # Wait one second
  time.sleep(1)

  current_temp = weather_station.getCurrentTemp()
  display.setHours(0)
  display.setMinutes(current_temp)

  # Wait one second
  time.sleep(1)
