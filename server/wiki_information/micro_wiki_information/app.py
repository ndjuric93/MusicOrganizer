""" Flask application """
from micro_wiki_information import create_app
from micro_wiki_information.config import SERVER_CONFIG


SERVICE_NAME = 'MicroWikiInformation'

if __name__ == '__main__':
    app = create_app(name=SERVICE_NAME, **SERVER_CONFIG)
    app.run(host=SERVER_CONFIG['host'], port=SERVER_CONFIG['port'], debug=True)
