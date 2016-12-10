from Libs.SevenSegment import Display
from datetime import datetime
from Libs.Clock import Clock

display = Display()

"""Update the clock's display
"""
def showCurrentTime():
  display.setHours(datetime.now().hour);
  display.setMinutes(datetime.now().minute);
  display.setColon(True);

clock = Clock()


clock.onTick(showCurrentTime);
