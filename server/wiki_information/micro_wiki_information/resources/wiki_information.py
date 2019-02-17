import json

import requests

from flask import jsonify
from flask_restplus import Namespace, Resource

api = Namespace('WikiInformation')

WIKIPEDIA_API = 'https://en.wikipedia.org/api/rest_v1/page/summary/'


@api.route('/information/wiki/<string:title>')
class WikiInformation(Resource):

    def get(self, title):
        response = requests.get(WIKIPEDIA_API + title)
        info = json.loads(response.content)
        if 'extract' in info:
            information = info['extract']
            return jsonify({'information': information})
        return jsonify({'information': 'No Info Available'})
