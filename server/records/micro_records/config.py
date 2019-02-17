import os

SERVER_CONFIG = {
    'host': os.environ.get('SERVER_ADDRESS', '0.0.0.0'),
    'port': os.environ.get('SERVER_PORT', '5003')
}

DB_SETTINGS = {
    'user': os.environ.get('DB_USER', 'microuser'),
    'password': os.environ.get('DB_PASSWORD'),
    'name': 'records',
    'address': os.environ.get('DB_ADDRESS', 'db')
}

KAFKA_CONFIG = {
    'bootstrap_servers': os.environ.get('KAFKA_ADDRESS', '0.0.0.0:9092')
}

MUSIC_ROOT = os.environ.get('MUSIC_ROOT', '/music')

JWT_KEY = os.environ.get('JWT_KEY', 'my-secret-key')
