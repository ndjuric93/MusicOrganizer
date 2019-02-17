from flask_restplus import Api

from .track_statistics import api as statistics

api = Api(title='Statistics')
api.add_namespace(statistics)
