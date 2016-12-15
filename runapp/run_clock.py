from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock
from Libs.GStreamer import Speaker

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

"""Play music through the attached speaker
"""
def playMusic():
  global Is_Evening, Proper_Hour
  speaker.playList(["AmicusMeus.ogg", "TestTrack.ogg"]);

"""Show current temperature
"""
def switchWeatherStations():
  global Is_Evening, Proper_Hour
  display.setEvening(False);
  display.setHours(0);
  display.setColon(False);
  display.setMinutes(0);
  clock.waitAbout(3);


clock.onTick(showCurrentTime);
display.setBrightness(11);

clock.atTime(8, 30, playMusic);
