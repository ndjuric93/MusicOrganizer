import os
from multiprocessing import Process

from flask import Flask
from flask_restplus import Api
from flask_jwt_simple import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from micro_utils.api_gateway.routes import list_routes
from micro_utils.service_registry.registration import ServiceRegistry

from micro_statistics.config import DB_SETTINGS, JWT_KEY

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app(name, **kwargs):
    app = Flask(__name__)
    api = Api(app=app)
    _set_sqlalchemy(app)

    db.init_app(app=app)

    ma.init_app(app=app)
    jwt.init_app(app=app)

    app.config['JWT_SECRET_KEY'] = JWT_KEY

    from micro_statistics.resources import api as statistics
    api.add_namespace(statistics)

    with app.app_context():
        routes = list_routes(app)
        db.create_all()

    with ServiceRegistry() as registry:
        registry.register(name, os.environ['SERVICE_NAME'] + ':' + kwargs['port'], routes)

    return app


def _set_sqlalchemy(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = _create_database_uri()


def _create_database_uri():
    return ('postgresql://' +
            DB_SETTINGS['user'] + ':' + DB_SETTINGS['password'] +
            '@' + DB_SETTINGS['address'] +
            '/' + DB_SETTINGS['name'])
