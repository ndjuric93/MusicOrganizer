from flask_restplus import Namespace, Resource

from flask import request, jsonify, current_app
from flask_jwt_simple import jwt_required, get_jwt_identity

from kafka import KafkaProducer

from micro_utils.flask.jwt import resolve_jwt_identity
from micro_utils.messaging.adapters import TopicProducer
from micro_utils.proto.SimpleSong_pb2 import SimpleSong
from micro_utils.proto.Song_pb2 import Song

from micro_records.models import Track, Album, Artist
from micro_records.schemas import tracks_schema, track_schema
from micro_records.config import KAFKA_CONFIG

api = Namespace('', description='Tracks Lister')


@api.route('/album/<int:album>')
class Tracks(Resource):

    @jwt_required
    def get(self, album):
        tracks = Track.query.filter(Track.album_id == album).order_by(Track.track_number)
        schema = tracks_schema.dump(tracks).data
        return {'tracks': schema}

    @jwt_required
    def post(self, album):
        track, _, author = (Track.query
                                     .join(Album, Album.id==Track.album_id)
                                     .join(Artist, Artist.id==Album.artist_id)
                                     .add_columns(Album.name, Artist.name)
                                     .filter(Track.id == album).first())
        self._send_song(track=track)
        self._emit_song_played(track=track, author=author)
        return {'Status': 'Track ' + track.name + ' added'}, 200

    @staticmethod
    def _send_song(track):
        producer = KafkaProducer(**KAFKA_CONFIG)
        song = Song(
            name=track.name,
            path=track.path,
            user=resolve_jwt_identity(current_app)
        )
        producer.send(value=song.SerializeToString(), topic='playlist')
        producer.flush()

    @staticmethod
    def _emit_song_played(track, author):
        producer = KafkaProducer(**KAFKA_CONFIG)
        print('#########')
        print(track.genre)
        print('#########')
        song = SimpleSong(
            song_id=track.id,
            author=author,
            genre=track.genre,
            name=track.name)
        producer.send(value=song.SerializeToString(), topic='track_selected')
        producer.flush()
