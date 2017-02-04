from gmusicapi import Mobileclient
from gmusicapi import exceptions
import logging
from hackclock.config import configuration
import json

logger = logging.getLogger('google_music')

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
logger.addHandler(console)

class AudioStream:
    __username = configuration.get('google_username')
    __password = configuration.get('google_password')
    __track_prefetch = 15
    __client = None
    __playlist = []

    def __init__(self, station_id = 'IFL'):
        self.__client = Mobileclient()
        self.__client.login(self.__username, self.__password, Mobileclient.FROM_MAC_ADDRESS)
        self.__playlist = self.__fetchTrackIDs(station_id)

    def __del__(self):
        if self.__client:
            self.__client.logout()

    def __fetchTrackIDs(self, station_id):
        if not self.__client or not self.__client.is_authenticated():
            logger.error("Client is not authenticated!")
            return []

        tracklist = self.__client.get_station_tracks(station_id, num_tracks=self.__track_prefetch)
        logger.info("Received tracks: %r" % json.dumps(tracklist))

        songids = [track['id'] for track in tracklist if 'id' in track]
        nautids = [track['nid'] for track in tracklist if 'nid' in track]

        return songids + nautids

    def pop(self):
        while self.__playlist:
            try:
                track_id = self.__playlist.pop()
                stream_url = self.__client.get_stream_url(track_id, quality='low')
                return stream_url
            except(exceptions.CallFailure):
                logger.warning("Failed to fetch Stream URL for ID %s" % trackid)

            raise IndexError("pop from empty list")

    def reverse(self):
        # Reverse just returns itself, since the playlist is already chaos
        return self

    def __len__(self):
        return len(self.__playlist)
