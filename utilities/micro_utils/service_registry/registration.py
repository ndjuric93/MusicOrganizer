import os

from kazoo.client import KazooClient as Client

from micro_utils.proto.ServiceLocation_pb2 import ServiceLocation

_SERVICE_NODE = 'services'
_ZOOKEEPER_ADDRESS = os.environ.get('ZOOKEEPER_ADDRESS', '0.0.0.0:2181')


class ServiceRegistry(object):
    client = Client(hosts=_ZOOKEEPER_ADDRESS, timeout=40)

    def __enter__(self):
        try:
            self.client.start()
            if not self.client.exists(path=_SERVICE_NODE):
                self.client.create(path=_SERVICE_NODE)
        except:
            pass
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.client.stop()

    def register(self, name, address, routes):
        msg = ServiceLocation(name=name, address=address, routes=routes)
        name = _SERVICE_NODE + '/' + name
        if self.client.exists(path=name):
            self.client.set(path=name, value=msg.SerializeToString())
        else:
            self.client.create(path=name, value=msg.SerializeToString())

    def unregister(self, name):
        if self.client.exists(path=name):
            self.client.delete(path=name)

    @property
    def services(self):
        services = {}
        for children in self.client.get_children(path=_SERVICE_NODE):
            data, _ = self.client.get(path=_SERVICE_NODE + '/' + children)
            location = ServiceLocation()
            location.ParseFromString(data)
            services[location.name] = {
                'address': location.address,
                'routes': location.routes
            }
        return services

    def get_service_address(self, name):
        return self.services[name]
