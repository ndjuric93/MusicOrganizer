""" Flask application """
from micro_records import create_app
from micro_records.config import SERVER_CONFIG


SERVICE_NAME = 'MicroRecords'

if __name__ == '__main__':
    app = create_app(name=SERVICE_NAME, **SERVER_CONFIG)
    app.run(host=SERVER_CONFIG['host'], port=SERVER_CONFIG['port'], debug=True)
