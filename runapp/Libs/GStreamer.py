import pygst
pygst.require('0.10')
import gst
import os
from config import configuration

class Speaker():

    def __init__(self):
        self.pl = None

    def play(self, fileName):
        self.pl = gst.element_factory_make("playbin", "player")
        audio_dir = configuration.get('audio_files')
        filePath = "%s/%s" % (audio_dir, fileName)
        self.pl.set_state(gst.STATE_READY)
        self.pl.set_property('uri','file://'+os.path.abspath(filePath))
        self.pl.set_state(gst.STATE_PLAYING)

    def stop(self):
        self.pl.set_state(gst.STATE_READY)

    def isPlaying(self):
        return gst.STATE_PLAYING in self.pl.get_state() if self.pl else False

