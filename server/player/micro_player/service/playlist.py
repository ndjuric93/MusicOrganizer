""" Playlist Manager class """
import json

from threading import Lock
from multiprocessing import Process
from flask import current_app

from redis import Redis
from kafka import KafkaConsumer

from micro_utils.messaging.kafka import publish_message, consume_messages
from micro_utils.messaging.adapters import TopicConsumer
from micro_utils.proto.utils import parse_song
from micro_utils.flask.jwt import resolve_jwt_identity

from micro_player.config import KAFKA_SERVER, REDIS_CONFIG

PLAYLIST = 'playlist'
INDEX = 'index'
MAX_SONG_LIMIT = 100

class PlaylistManager:
    """
    This class is supposed to take care of user songs
    Playlist is stored in redis.
    Every user has an index and his list of song.
    Every path of song has a key with value of the song name.
    Songs are consumed from kafka queue.
    """

    def __init__(self):
        """ Initiates redis connection and starts consuming process """
        self.redis = Redis(host=REDIS_CONFIG['address'])
        Process(target=self._collect).start()
        self.lock = Lock()

    def set_index(self, user_id, index):
        """
        Sets index in the playlist for user
        TODO: Raise an exception when index is unavailable
        """
        self.redis.set(PLAYLIST + '_' + user_id, index)

    def update_index(self, user_id):
        """ Updates index when song is finished """
        self.set_index(user_id, self._get_user_index(user_id) + 1)

    def get_song(self, user_id, song_id):
        """ Gets specific song for given user """
        return self.redis.lrange(user_id, 0, MAX_SONG_LIMIT)[song_id]

    def get_song_name(self, user_id, song_id):
        """ Gets whole playlist for given user """
        return [name.decode() for name in self._get_song_names(user_id)][self._get_user_index(user_id)]


    def get_playlist_for_user(self, user_id):
        """ Gets whole playlist for given user """
        if self.redis.get(PLAYLIST + '_' + user_id) is None:
            self.redis.set(PLAYLIST + '_' + user_id, 0)

        return {
            PLAYLIST: [name.decode() for name in self._get_song_names(user_id)],
            INDEX: self._get_user_index(user_id)
        }

    def delete_song(self, user_id, song_id):
        """ Deletes the song from redis list """
        with self.lock:
            self.redis.lset(user_id, song_id, 'TO_DELETE')
            self.redis.lrem(user_id, 1, 'TO_DELETE')

    def _get_user_index(self, user_id):
        return int(self.redis.get(PLAYLIST + '_' + user_id))

    def _collect(self):
        consumer = KafkaConsumer(
            group_id='playlist',
            **KAFKA_SERVER
        )
        consumer.subscribe(topics=('playlist',))
        self._consume(consumer)

    def _consume(self, consumer):
        while True:
            for message in consumer:
                song = parse_song(message)
                self._add_song(song=song)

    def _add_song(self, song):
        """ TODO: Records will send a message with particular TYPES, so TO END will add to end"""
        self.redis.rpush(song.user, song.path)
        self.redis.set(song.path, song.name)

    def _get_song_names(self, user_id):
        playlist_paths = self.redis.lrange(user_id, 0, MAX_SONG_LIMIT)
        return [self.redis.get(path) for path in playlist_paths]
