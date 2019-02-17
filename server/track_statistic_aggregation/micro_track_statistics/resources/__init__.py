from flask_restplus import Api

from .track_statistics_aggregation import api as track_statistics

api = Api(title='TrackStatistics')
api.add_namespace(track_statistics)
