""" Flask application """
from micro_player import create_app
from micro_player.config import SERVER_CONFIG

SERVICE_NAME = 'MicroPlayer'

if __name__ == '__main__':
    app = create_app(name=SERVICE_NAME, **SERVER_CONFIG)
    app.run(
        host=SERVER_CONFIG['host'],
        port=SERVER_CONFIG['port'],
        debug=True
    )
