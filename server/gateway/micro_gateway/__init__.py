import os

from flask import Flask
from flask_restplus import Api
from flask_jwt_simple import JWTManager
from flask_cors import CORS

SERVICE_NAME = 'MicroGateway'

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    CORS(app)
    jwt.init_app(app=app)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY', 'my-secret-key')
    app.config['PROPAGATE_EXCEPTIONS'] = True
    api = Api(app=app)

    from micro_gateway.resources import api as gateway

    api.add_namespace(gateway)

    return app
