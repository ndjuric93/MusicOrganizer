import os

from flask import Flask, Response
from flask_cors import CORS
from flask_restplus import Api
from flask_jwt_simple import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from celery import Celery

from micro_utils.api_gateway.routes import list_routes
from micro_utils.service_registry.registration import ServiceRegistry

from micro_records.config import DB_SETTINGS, JWT_KEY

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
celery = Celery('', broker='redis://redis')

def create_app(name, **kwargs):
    app = Flask(__name__)
    _set_sqlalchemy(app=app)


    CORS(app)
    api = Api(app=app)

    db.init_app(app=app)
    ma.init_app(app=app)

    jwt.init_app(app=app)
    jwt._set_error_handler_callbacks(api)

    app.config['JWT_SECRET_KEY'] = JWT_KEY
    # Enables jwt to propagate exceptions
    app.config['PROPAGATE_EXCEPTIONS'] = True


    from micro_records.resources import api as records
    api.add_namespace(records)

    with app.app_context():
        routes = list_routes(app)
        print(routes, flush=True)
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
