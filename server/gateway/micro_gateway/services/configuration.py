""" Gateway configuration will be set up in yaml format """
import os
from itertools import chain

import yaml


class ConfigurationParser(object):

    def __init__(self):
        super(ConfigurationParser, self).__init__()
        with open(os.getenv('GATEWAY_CONFIG', 'gateway.yaml')) as gateway_config:
            self.config = yaml.load(gateway_config)

    @property
    def routes(self):
        return list(chain(*self._get_routes(self.config['microservices'])))

    @staticmethod
    def _get_routes(microservices):
        return [info['routes'] for info in microservices.values()]


config = ConfigurationParser()
