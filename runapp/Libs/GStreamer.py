import threading
import time
import pygst
pygst.require('0.10')
import gst
import os
from config import configuration

class Speaker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.pl = None
        self.daemon = True
        self.start()

    def play(self, fileName):
        if not self.isPlaying():
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

    def run(self):
        position = -1
        last_position = -2

        while True:
            time.sleep(1)
            if self.isPlaying():
                if position > last_position: # Is the song done playing?
                    last_position = position
                    position, format = self.pl.query_position(gst.FORMAT_TIME)
                else: # If so, shut the stream down
                    position = -1
                    last_position = -2
                    return self.stop()
