from Libs.Input import Button
from Libs.GStreamer import Speaker

gpio_24 = Button(24)
gpio_23 = Button(23)

speaker = Speaker()

"""Describe this function...
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

gpio_23.whenPressed(playStopMusic)
gpio_24.whenPressed(playStopMusic)
