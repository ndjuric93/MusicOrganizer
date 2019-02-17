import os

SERVER_CONFIG = {
    'host': os.environ.get('SERVER_ADDRESS', '0.0.0.0'),
    'port': os.environ.get('SERVER_PORT', '5001')
}

KAFKA_SERVER = {
    'bootstrap_servers': os.environ.get('KAFKA_ADDRESS', '0.0.0.0:9092')
}

KAFKA_CONFIG = {
    'bootstrap_servers': os.environ.get('KAFKA_ADDRESS', '0.0.0.0:9092')
}


REDIS_CONFIG = {
    'address': os.environ.get('REDIS_ADDRESS', '0.0.0.0')
}

JWT_KEY = os.environ.get('JWT_KEY', 'my-secret-key')
