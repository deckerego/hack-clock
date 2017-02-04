#/bin/python

print "Loading Libraries"
from GoogleMusic import AudioStream
import pygst
pygst.require('0.10')
import gst

def on_tag(bus, msg):
    taglist = msg.parse_tag()
    print 'on_tag:'
    for key in taglist.keys():
        print '\t%s = %s' % (key, taglist[key])

print "Initializing Google Music"
audio_stream = AudioStream()

print "Initializing Player"
player = gst.element_factory_make("playbin", "player")
player.set_state(gst.STATE_READY)
player.set_property('uri', audio_stream.pop())
player.set_state(gst.STATE_PLAYING)

print "Monitoring Bus"
bus = player.get_bus()
bus.enable_sync_message_emission()
bus.add_signal_watch()
bus.connect('message::tag', on_tag)

raw_input('Press enter to stop playing...')