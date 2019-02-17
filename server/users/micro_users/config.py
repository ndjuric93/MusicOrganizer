import os

SERVER_CONFIG = {
    'host': os.environ.get('SERVER_ADDRESS', '0.0.0.0'),
    'port': os.environ.get('SERVER_PORT', '5001')
}

DB_SETTINGS = {
    'user': os.environ.get('DB_USER', 'microuser'),
    'password': os.environ.get('DB_PASSWORD'),
    'name': 'records',
    'address': os.environ.get('DB_ADDRESS', 'db')
}

JWT_KEY = os.environ.get('JWT_KEY', 'my-secret-key')
