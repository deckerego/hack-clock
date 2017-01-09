from datetime import datetime
from Libs.SevenSegment import Display
from Libs.Clock import Clock
import random
from Libs.GStreamer import Speaker
from Libs.Input import Button

Is_Evening = None
songs = None

display = Display()

"""Display the current time
"""
def showCurrentTime():
  global Is_Evening, songs
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
  global Is_Evening, songs
  songs = ["AmicusMeus.ogg", "TestTrack.ogg"]
  random.shuffle(songs)
  speaker.playList(songs)

gpio_23 = Button(23)
gpio_24 = Button(24)

"""Stop music if playing, otherwise start music
"""
def playStopMusic():
  global Is_Evening, songs
  if speaker.isPlaying():
    speaker.stop()
  else:
    playMusic()


clock.onTick(showCurrentTime)
display.setBrightness(13)

clock.atTime(8, 30, playMusic)

gpio_23.whenPressed(playStopMusic)
gpio_24.whenPressed(playStopMusic)
