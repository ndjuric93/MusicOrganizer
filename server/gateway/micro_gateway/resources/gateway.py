import json
from itertools import chain, groupby

from requests import get, post, put, delete

from flask import request, Response

from flask_restplus import Namespace, Resource

from micro_gateway.services.service_router import get_service_path
from micro_gateway.services.configuration import config
from micro_gateway.services.aggregations import route_aggregations

api = Namespace('')
config_routes = config.routes


@api.route('/')
@api.route('/<path:url_path>')
class Gateway(Resource):

    def get(self, url_path=''):
        return self._create_request(method_func=get, url_path=url_path)

    def post(self, url_path=''):
        return self._create_request(method_func=post, url_path=url_path)

    def put(self, url_path=''):
        return self._create_request(method_func=put, url_path=url_path)

    def delete(self, url_path=''):
        return self._create_request(method_func=delete, url_path=url_path)

    def _create_request(self, method_func, url_path=''):
        # TODO: How to deal with multiple responses better, x-multipart might be solution
        if url_path in route_aggregations:
            return self._perform_multiple_requests(url_path, method_func)
        path = 'http://' + get_service_path(url_path) + '/' + url_path
        resp = method_func(path, json=api.payload, headers=request.headers, params=request.args)
        return Response(resp, mimetype=resp.headers['Content-Type'], status=resp.status_code)

    def _perform_multiple_requests(self, url_path, method_func):
        aggregated_routes = self._resolve_routes(url_path)
        resp = {
            'response': {},
            'status': []
        }
        for route in aggregated_routes['routes']:
            self._send_request(route, resp, method_func)
        if self._check_status(resp):
            return Response('Error', mimetype=resp['headers'], status=400)
        return Response(json.dumps(resp['response']), mimetype=resp['headers'], status=resp['status'])

    def _send_request(self, route, resp, method_func):
        path = 'http://' + get_service_path(route) + '/' + route
        response = method_func(path, json=api.payload, headers=request.headers, params=request.args)
        self._update_response(resp, response)

    def _update_response(self, resp, response):
        resp['response'] = dict(chain(resp['response'].items(), response.json().items()))
        resp['headers'] = response.headers['Content-Type']
        resp['status'].append(response.status_code)

    def _check_status(self, resp):
        for status in resp['status']:
            if status >= 400:
                resp['status'] = status
                return True
        resp['status'] = resp['status'].pop()
        return False

    def _resolve_routes(self, url_path):
        if url_path in route_aggregations:
            return route_aggregations[url_path]
        return {
            'routes': [url_path],
        }

