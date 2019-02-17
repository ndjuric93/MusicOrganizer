""" Gateway configuration will be set up in yaml format """
import os
from itertools import chain

import yaml

def load_aggregations():
    return {}
#     with open(os.getenv('GATEWAY_CONFIG', 'gateway.yaml')) as gateway_config:
#         return yaml.load(gateway_config)['aggregations']

route_aggregations = load_aggregations()
