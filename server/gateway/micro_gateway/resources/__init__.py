from flask_restplus import Api

from .gateway import api as gateway

api = Api(title='Gateway')
api.add_namespace(gateway)
