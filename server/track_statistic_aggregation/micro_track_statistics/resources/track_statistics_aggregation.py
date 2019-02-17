import requests

from flask import request
from flask_restplus import Namespace, Resource
from flask_jwt_simple import jwt_required, get_jwt

from micro_utils.service_registry import ServiceRegistry

api = Namespace('', description='TrackStatisticsAggregation')


@api.route('/track/statistics/<int:album>')
class TrackStatisticsAggregation(Resource):

    @jwt_required
    def get(self, album):
        with ServiceRegistry() as registry:
            tracks = registry.get_service_address('MicroRecords')
            statistics = registry.get_service_address('MicroStatistics')
        track_response = requests.get(
            'http://' + tracks['address'] + '/album/' + str(album),
            headers=request.headers
        )
        statistics_response = requests.get(
            'http://' + statistics['address'] + '/statistics',
            headers=request.headers
        )
        stats = self._convert_statistics(statistics_response.json()['tracks_selected'])
        tracks = track_response.json()
        self._aggregate(tracks['tracks'], stats)
        return tracks, 200

    def _convert_statistics(self, statistics):
        return {
            track['id']: track['count'] for track in statistics
        }

    def _aggregate(self, tracks, statistics):
        for track in tracks:
            track['count'] = (
                statistics[track['id']] if track['id'] in statistics.keys() else 0
            )
