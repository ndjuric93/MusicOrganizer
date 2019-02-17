import os

from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_simple import JWTManager

from micro_player.service.playlist import PlaylistManager
from micro_player.config import REDIS_CONFIG, JWT_KEY

from micro_utils.api_gateway.routes import list_routes
from micro_utils.service_registry import ServiceRegistry


playlist = PlaylistManager()
jwt = JWTManager()

def create_app(name, **kwargs):
    app = Flask(__name__)
    CORS(app)
    api = Api(app=app)
    jwt.init_app(app=app)
    app.config['JWT_SECRET_KEY'] = JWT_KEY

    from micro_player.resources import api as player
    api.add_namespace(player)

    with app.app_context():
        routes = list_routes(app)

    with ServiceRegistry() as registry:
        registry.register(name,  os.environ['SERVICE_NAME'] + ':' + kwargs['port'], routes)

    return app
