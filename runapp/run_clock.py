from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock
from Libs.GStreamer import Speaker

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


clock.atTime(8, 30, playMusic);

clock.onTick(showCurrentTime);
display.setBrightness(13);
