from Libs.Input import Button
from Libs.GStreamer import Speaker

gpio_24 = Button(24)

speaker = Speaker()

"""Describe this function...
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
