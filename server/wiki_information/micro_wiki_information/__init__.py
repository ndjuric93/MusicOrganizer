import os

from flask import Flask
from flask_restplus import Api
from flask_jwt_simple import JWTManager

from micro_utils.api_gateway.routes import list_routes
from micro_utils.service_registry.registration import ServiceRegistry

jwt = JWTManager()

def create_app(name, **kwargs):
    app = Flask(__name__)

    api = Api(app=app)
    jwt.init_app(app=app)

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY', 'my-secret-key')

    with app.app_context():
        routes = list_routes(app)

    from micro_wiki_information.resources import api as wiki_information
    api.add_namespace(wiki_information)

    # with ServiceRegistry() as registry:
    #     registry.register(name, os.environ['SERVICE_NAME'] + ':' + kwargs['port'], routes)

    return app