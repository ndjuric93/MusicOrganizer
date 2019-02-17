from flask_restplus import Namespace, Resource

from flask_jwt_simple import jwt_required

from micro_records.models import Artist
from micro_records.schemas import artists_schema

api = Namespace('', description='Artist Fetcher')


@api.route('/artist')
class Artists(Resource):

    @jwt_required
    def get(self):
        artists = artists_schema.dump(Artist.query.all()).data
        return {'artists': artists}
