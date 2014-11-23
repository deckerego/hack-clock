#!/usr/bin/python

import time
import datetime
from ClockDisplay import ClockDisplay

# Connect to the LED display
display = ClockDisplay(address=0x70)

# Set the brightness (0 to 15, 15 is the brightest)
display.setBrightness(5)

# Set the colon in the middle
display.setColon(True)

# Keep updating, never stop
while(True):
  now = datetime.datetime.now()

  is_evening = now.hour > 12
  display.setHours(now.hour if not is_evening else now.hour - 12)
  display.setEvening(is_evening)

  display.setMinutes(now.minute)

  # Wait one second
  time.sleep(1)
