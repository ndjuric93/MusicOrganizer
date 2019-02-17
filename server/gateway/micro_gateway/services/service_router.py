from flask import abort

from micro_utils.service_registry import ServiceRegistry
from micro_gateway.services.configuration import config

routes = config.routes


def get_service_path(route):
    with ServiceRegistry() as registry:
        services = registry.services
        for _, data in services.items():
            for available_route in data['routes']:
                if route.startswith(available_route.split('/')[0]):
                    return data['address']
    abort(404)
