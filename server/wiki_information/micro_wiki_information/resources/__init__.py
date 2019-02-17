from flask_restplus import Api

from .wiki_information import api as wiki_information

api = Api(title='Wiki information')
api.add_namespace(wiki_information)
