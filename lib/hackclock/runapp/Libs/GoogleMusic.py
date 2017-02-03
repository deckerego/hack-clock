from gmusicapi import Mobileclient
from GStreamer import Speaker
import logging
from hackclock.config import configuration

logger = logging.getLogger('google_music')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

class GoogleMusic:
    __username = configuration.get('google_username')
    __password = configuration.get('google_password')
    __track_prefetch = 25
    __client = None

    def __init__(self):
        self.__client = Mobileclient()
        self.__client.login(self.__username, self.__password, Mobileclient.FROM_MAC_ADDRESS)

    def __del__(self):
        if self.__client:
            self.__client.logout()

    def radioPlaylist(self, station_id = 'IFL'):
        if not self.__client or not self.__client.is_authenticated():
            logger.error("Client is not authenticated!")
            return []

        tracklist = self.__client.get_station_tracks(station_id, num_tracks=self.__track_prefetch)
        logger.info("Received tracks: %r" % str(tracklist))

        trackidlist = [track['id'] for track in tracklist if 'id' in track]
        return [self.__client.get_stream_url(trackid, quality='low') for trackid in trackidlist]
