import threading
import time
import pygst
pygst.require('0.10')
import gst
import gobject
import os
from config import configuration

class Speaker:

    def __init__(self):
        self.pl = None
        self.eventLoop = None
        gobject.threads_init()

    def play(self, fileName):
        if not self.isPlaying():
            # Create a queue of URIs
            audio_dir = configuration.get('audio_files')
            files = [ fileName ] # TODO Remove this for playlist support
            self.playlist = [ "file://"+os.path.abspath("%s/%s" % (audio_dir, fileName)) for file in files ]
            self.playlist.reverse()

            # Create the pipeline
            self.pl = gst.element_factory_make("playbin2", "player")
            self.pl.set_state(gst.STATE_READY)
            self.pl.connect("about-to-finish", self.aboutToFinish)

            # Create the event bus
            self.bus = self.pl.get_bus()
            self.bus.add_signal_watch()
            self.bus.connect("message", self.onMessage)
            self.eventLoop = GtkEventLoop()
            self.eventLoop.start()

            # Play next track on playlist
            self.pl.set_property('uri', self.playlist.pop())
            self.pl.set_state(gst.STATE_PLAYING)

    def stop(self):
        self.pl.set_state(gst.STATE_NULL)
        if self.eventLoop: self.eventLoop.quit()

    def isPlaying(self):
        return gst.STATE_PLAYING in self.pl.get_state() if self.pl else False

    def aboutToFinish(self, player):
        if self.playlist:
            self.pl.set_property('uri', self.playlist.pop())

    def onMessage(self, bus, message):
        if message.type == gst.MESSAGE_EOS:
            self.stop()

class GtkEventLoop(threading.Thread):

    def __init__(self):
        self.loop = gobject.MainLoop()
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        self.loop.run()

    def quit(self):
        self.loop.quit()
