import os
import unittest
import subprocess

from kazoo.client import KazooClient

from micro_utils.service_registry.registration import ServiceRegistry

_SERVICE_NODE = 'services'
_DEFAULT_ZOOKEEPER_ADDRESS = '0.0.0.0:2181'


class TestServiceRegistry(unittest.TestCase):

    _TEST_SERVICE_NODE = 'test_ms'
    _TEST_SERVICE_ADDRESS = '127.0.0.1:5000'
    _TEST_SERVICE_ROUTE = ['/home', '/away']

    @classmethod
    def setUpClass(cls):
        subprocess.Popen('start_zookeeper', env=dict(os.environ))
        cls.test_client = KazooClient(hosts=_DEFAULT_ZOOKEEPER_ADDRESS)
        cls.test_client.start()
        if not cls.test_client.exists(_SERVICE_NODE):
            cls.test_client.create(_SERVICE_NODE)

    @classmethod
    def tearDownClass(cls):
        subprocess.Popen('stop_zookeeper', env=dict(os.environ))
        if cls.test_client.exists(_SERVICE_NODE):
            cls.test_client.delete(_SERVICE_NODE, recursive=True)
        cls.test_client.stop()

    def test_register(self):
        with ServiceRegistry() as service_registry:
            service_registry.register(self._TEST_SERVICE_NODE, self._TEST_SERVICE_ADDRESS, self._TEST_SERVICE_ROUTE)
        self.assertTrue(TestServiceRegistry.test_client.exists(_SERVICE_NODE + '/' + self._TEST_SERVICE_NODE))

    def test_unregister(self):
        with ServiceRegistry() as service_registry:
            service_registry.register(self._TEST_SERVICE_NODE, self._TEST_SERVICE_ADDRESS, self._TEST_SERVICE_ROUTE)
            service_registry.unregister(self._TEST_SERVICE_NODE + '/' + self._TEST_SERVICE_ADDRESS)
        self.assertFalse(TestServiceRegistry.test_client.exists(self._TEST_SERVICE_NODE))

    def test_get_services(self):
        nodes = [self._TEST_SERVICE_NODE + '_1', self._TEST_SERVICE_NODE + '_2']
        address = 'test_address'
        with ServiceRegistry() as service_registry:
            service_registry.register(nodes[0], address, ['test_data_1'])
            service_registry.register(nodes[1], address, ['test_data_2'])
            data = service_registry.get_services
        print(data.keys())
        zookeeper_nodes = data.keys()
        for node in nodes:
            self.assertIn(node, zookeeper_nodes)

