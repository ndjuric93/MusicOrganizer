""" Playlist flask resources """
import json

from flask import Response, current_app, jsonify
from flask_restplus import Resource, Namespace
from flask_jwt_simple import jwt_required, get_jwt_identity

from micro_utils.flask.jwt import resolve_jwt_identity

from micro_player import playlist

api = Namespace('')

@api.route('/playlist')
class Playlist(Resource):

    @jwt_required
    def get(self):
        user_identity = resolve_jwt_identity(current_app)
        user_playlist = playlist.get_playlist_for_user(user_id=user_identity)
        return Response(json.dumps(user_playlist), status=200)

    @jwt_required
    def post(self):
        playlist.update_index(resolve_jwt_identity(current_app))
        return Response('Success', status=200)

@api.route('/playlist/<int:index>')
class PlaylistIndex(Resource):

    def post(self, index):
        playlist.set_index(resolve_jwt_identity(current_app), index)
        return Response({'playlist_index': index}, status=200)

@api.route('/playlist/<int:song_index>')
class PlaylistTrack(Resource):

    @jwt_required
    def delete(self, song_index):
        playlist.delete_song(resolve_jwt_identity(current_app), song_index)
