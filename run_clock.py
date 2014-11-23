#!/usr/bin/python

import time
import datetime
from Adafruit.SevenSegment import SevenSegment

# Connect to the LED display
segment = SevenSegment(address=0x70)

# Keep updating, never stop
while(True):
  now = datetime.datetime.now()

  # Set hours
  segment.writeDigit(0, int(now.hour / 10))     # Tens
  segment.writeDigit(1, now.hour % 10)          # Ones

  # Set minutes
  segment.writeDigit(3, int(now.minute / 10))   # Tens
  segment.writeDigit(4, now.minute % 10)        # Ones

  # Wait one second
  time.sleep(1)
