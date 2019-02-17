import json

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from flask import jsonify
from flask_restplus import Namespace, Resource
from flask_jwt_simple import jwt_required

from micro_records.service.track_collector import collect_tracks
from micro_records.service.track_finder import walk_directory

api = Namespace('', description='Track collector')


@api.route('/refresh_tracks')
class RefreshTracks(Resource):

    def post(self):
        try:
            # walk_directory.delay()
            tracks = collect_tracks()
            return jsonify({'Status': json.dumps(tracks)})
        except (IntegrityError, NoResultFound):
            return jsonify({'Status': 'Failed'})
