from micro_utils.api_gateway.routes import list_routes
import os

from . import messaging, proto

KAFKA_IP = os.environ['KAFKA_ADDRESS'] if os.environ.get('KAFKA_ADDRESS') is not None else '0.0.0.0'
KAFKA_PORT = os.environ['KAFKA_PORT'] if os.environ.get('KAFKA_PORT') is not None else '9092'

KAFKA_ADDRESS = KAFKA_IP + ':' + KAFKA_PORT

KAFKA_CONFIG = {
    'bootstrap.servers': KAFKA_ADDRESS,
    'group.id': 1,
    'auto.offset.reset': 'earliest'
}
