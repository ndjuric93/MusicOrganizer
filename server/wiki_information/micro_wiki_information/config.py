import os

SERVER_CONFIG = {
    'host': os.environ.get('SERVER_ADDRESS', '0.0.0.0'),
    'port': os.environ.get('SERVER_PORT', '5006')
}

JWT_KEY = os.environ.get('JWT_KEY', 'my-secret-key')
