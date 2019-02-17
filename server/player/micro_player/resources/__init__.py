from flask_restplus import Api

from .player import api as player
from .playlist import api as playlist

api = Api(title='Player')
api.add_namespace(player)
api.add_namespace(playlist)
