''' Flask application '''
import os
from micro_gateway import create_app

from micro_gateway.config import SERVER_CONFIG

if __name__ == '__main__':
    app = create_app()
    app.run(host=SERVER_CONFIG['host'], port=SERVER_CONFIG['port'], debug=True)
