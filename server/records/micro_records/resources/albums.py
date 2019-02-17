from flask_restplus import Namespace, Resource

from flask_jwt_simple import jwt_required, get_jwt_identity

from micro_records.models import Album, Artist
from micro_records.schemas import albums_schema

api = Namespace('', description='Album Fetcher')


@api.route('/artist/<int:artist_id>')
class Albums(Resource):

    @jwt_required
    def get(self, artist_id):
        albums = Album.query.filter(Album.artist_id == artist_id).all()
        return {'albums': albums_schema.dump(albums).data}
