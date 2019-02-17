from flask_restplus import Resource, Namespace

from micro_users.models import BaseUser
from micro_users.schemas import users_schema

api = Namespace('')


@api.route('/users')
class Users(Resource):

    @api.doc('Returns a list of uses')
    def get(self):
        users = BaseUser.query.all()
        return {'users': users_schema.dump(users).data}
