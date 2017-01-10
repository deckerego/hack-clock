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

"""Wake up only on weekdays
"""
def wakeUp():
  global Is_Evening, songs
  if not (datetime.now().weekday() in (5, 6)):
    playMusic()

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

clock.atTime(7, 0, wakeUp)

gpio_24.whenPressed(playStopMusic)
