from flask import Response
from flask_restplus import Namespace, Resource

from sqlalchemy import desc

from flask_jwt_simple import jwt_required, get_jwt_identity

from micro_statistics import db
from micro_statistics.models import TrackSelectedCount
from micro_statistics.models import TrackPlayedCount
from micro_statistics.models import GenreSelected
from micro_statistics.schemas.tracks_selected import track_selected
from micro_statistics.schemas.genre_selected import genre_count
from micro_statistics.schemas.tracks_played import track_played


api = Namespace('', description='TrackStatistics')

@api.route('/statistics/count')
class CountStatistics(Resource):

    def get(self):
        most_played = TrackSelectedCount.query.order_by(desc(TrackSelectedCount.count)).limit(1).first()
        return {
            'most_played': {
                'count': most_played.count,
                'author': most_played.author,
                'name': most_played.name
            }
        }

@api.route('/statistics/count/author')
class MostPlayerAuthor(Resource):

    def get(self):
        most_played = TrackSelectedCount.query.order_by(desc(TrackSelectedCount.count)).limit(1).first()
        return {
            'most_played': {
                'count': most_played.count,
                'author': most_played.author,
                'name': most_played.name
            }
        }


@api.route('/statistics')
class Statistics(Resource):

    def get(self):
        tracks_selected = TrackSelectedCount.query.all()
        tracks_played = TrackPlayedCount.query.all()
        genre_selected = GenreSelected.query.all()
        return {
            'tracks_selected': track_selected.dump(tracks_selected).data,
            'tracks_played': track_played.dump(tracks_played).data,
            'genre_selected': genre_count.dump(genre_selected).data
        }
