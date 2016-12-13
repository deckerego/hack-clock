from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock

Is_Evening = None
Proper_Hour = None

display = Display()

"""Update the clock's display
"""
def showCurrentTime():
  global Is_Evening, Proper_Hour
  Is_Evening = datetime.now().hour >= 12
  Proper_Hour = datetime.now().hour - 12 if Is_Evening else datetime.now().hour
  display.setHours(Proper_Hour);
  display.setColon(Is_Evening);
  display.setMinutes(datetime.now().minute);

clock = Clock()


clock.onTick(showCurrentTime);
display.setBrightness(11);
