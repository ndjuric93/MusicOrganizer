from flask import Response, current_app
from flask_restplus import Resource, Namespace
from flask_jwt_simple import jwt_required, get_jwt_identity

from kafka import KafkaProducer

from micro_utils.proto.SimpleSong_pb2 import SimpleSong
from micro_utils.proto.Song_pb2 import Song
from micro_utils.flask.jwt import resolve_jwt_identity

from micro_player import playlist
from micro_player.config import KAFKA_SERVER

api = Namespace('')

DATA_TO_STREAM = 1024


@api.route('/player/<int:song_id>')
class Player(Resource):

    def get(self, song_id):
        song = playlist.get_song(resolve_jwt_identity(current_app), song_id)
        if song is None:
            return Response('No song available', status=400)

        return Response(Player.play_song(song), mimetype="audio/mp3", status=200)

    def post(self, song_id):
        song = playlist.get_song_name(resolve_jwt_identity(current_app), song_id)
        producer = KafkaProducer(**KAFKA_SERVER)
        song = Song(
            name=song,
        )
        producer.send(value=song.SerializeToString(), topic='song_played')
        producer.flush()

        return Response('Success', status=200)

    @staticmethod
    def play_song(path):
        with open(path, "rb") as song:
            data = song.read(DATA_TO_STREAM)
            while data:
                yield data
                data = song.read(DATA_TO_STREAM)
