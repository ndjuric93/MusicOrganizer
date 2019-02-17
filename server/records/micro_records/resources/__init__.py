from flask_restplus import Api

from .artists import api as artists
from .albums import api as albums
from .tracks import api as tracks
from .collect import api as collect

api = Api(title='Records')
api.add_namespace(artists)
api.add_namespace(albums)
api.add_namespace(tracks)
api.add_namespace(collect)
