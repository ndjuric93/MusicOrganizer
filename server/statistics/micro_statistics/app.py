""" Flask application """
from micro_statistics import create_app
from micro_statistics.config import SERVER_CONFIG
from micro_statistics.services.playing_listener import start_selection_listening

SERVICE_NAME = 'MicroStatistics'

if __name__ == '__main__':
    app = create_app(name=SERVICE_NAME, **SERVER_CONFIG)
    start_selection_listening(app)
    app.run(host='0.0.0.0', port='5004', debug=True)