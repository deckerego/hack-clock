from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock
from Libs.GStreamer import Speaker
from Libs.Input import Button

Is_Evening = None

display = Display()

"""Describe this function...
"""
def showCurrentTime():
  global Is_Evening
  Is_Evening = datetime.now().hour > 12
  display.setHours((datetime.now().hour - 12 if Is_Evening else datetime.now().hour));
  display.setColon(True);
  display.setEvening(Is_Evening);
  display.setMinutes(datetime.now().minute);

clock = Clock()

speaker = Speaker()

"""Play audio files through the speaker
"""
def playMusic():
  global Is_Evening
  speaker.playList(["AmicusMeus.ogg", "TestTrack.ogg"]);

"""Describe this function...
"""
def switchWeatherStations():
  global Is_Evening
  display.setColon(False);
  display.setEvening(False);
  display.setMinutes(0);
  display.setMinutes(0);
  clock.waitAbout(3);

gpio_24 = Button(24)


clock.onTick(showCurrentTime);
display.setBrightness(13);

clock.atTime(8, 30, playMusic);

gpio_24.whenPressed(switchWeatherStations);
