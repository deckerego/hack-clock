import threading
import time
import pygst
pygst.require('0.10')
import gst
import gobject
import os
import re
import logging
from hackclock.config import configuration

logger = logging.getLogger('speaker')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

class Speaker:
    __HTTP_PATTERN = re.compile("http[s]*://.*")

    def __init__(self):
        self.pl = None
        self.eventLoop = None
        gobject.threads_init()

    def play(self, fileName):
        self.playList([fileName])

    def playList(self, trackNames):
        if not self.isPlaying():
            self.playlist = trackNames
            self.playlist.reverse()
            self.play()

    def play(self):
        # Create the pipeline
        self.pl = gst.element_factory_make("playbin2", "player")
        self.pl.set_state(gst.STATE_READY)

        # Create the event bus
        self.bus = self.pl.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.onMessage)
        self.eventLoop = GtkEventLoop()
        self.eventLoop.start()

        # Play next track on playlist
        self.next()

    def stop(self):
        self.pl.set_state(gst.STATE_NULL)
        if self.eventLoop: self.eventLoop.quit()

    def isPlaying(self):
        return gst.STATE_PLAYING in self.pl.get_state() if self.pl else False

    def next(self):
        if self.playlist:
            track = self.playlist.pop()

            if not self.__HTTP_PATTERN.match(track):
                # This is a filename - convert to URI
                audio_dir = configuration.get('audio_files')
                track = "file://"+os.path.abspath("%s/%s" % (audio_dir, track))

            logger.info("Playing: %s" % track)
            self.pl.set_state(gst.STATE_READY)
            self.pl.set_property('uri', track)
            self.pl.set_state(gst.STATE_PLAYING)
        else:
            self.stop()

    def onMessage(self, bus, message):
        if message.type == gst.MESSAGE_EOS:
            self.next()

class GtkEventLoop(threading.Thread):

    def __init__(self):
        self.loop = gobject.MainLoop()
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        self.loop.run()

    def quit(self):
        self.loop.quit()
