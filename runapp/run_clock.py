from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock
from Libs.GStreamer import Speaker
from Libs.Input import Button
from Libs.Input import Switch

Is_Evening = None

display = Display()

"""Describe this function...
"""
def showCurrentTime():
  global Is_Evening
  Is_Evening = datetime.now().hour > 12
  display.setHours((datetime.now().hour - 12 if Is_Evening else datetime.now().hour))
  display.setColon(True)
  display.setEvening(Is_Evening)
  display.setMinutes(datetime.now().minute)

clock = Clock()

speaker = Speaker()

"""Play audio files through the speaker
"""
def playMusic():
  global Is_Evening
  speaker.playList(["AmicusMeus.ogg", "TestTrack.ogg"])

gpio_23 = Button(23)

gpio_25 = Switch(25)

"""Describe this function...
"""
def bright():
  global Is_Evening
  gpio_25.turnOn();
  display.setBrightness(15)

gpio_24 = Button(24)

"""Describe this function...
"""
def dim():
  global Is_Evening
  gpio_25.turnOff();
  display.setBrightness(3)


clock.onTick(showCurrentTime)
display.setBrightness(9)

clock.atTime(8, 30, playMusic)

gpio_23.whenPressed(dim)

gpio_24.whenPressed(bright)
