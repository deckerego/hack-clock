import pygst
pygst.require('0.10')
import gst
import os

import pygame

class Speaker():

    def __init__(self):
        self.pl = gst.element_factory_make("playbin", "player")

    def play(self, fileName):
        audio_dir = configuration.get('audio_files')
        filePath = "%s/%s" % (audio_dir, fileName)
        self.pl.set_property('uri','file://'+os.path.abspath(filePath))
        self.pl.set_state(gst.STATE_PLAYING)
