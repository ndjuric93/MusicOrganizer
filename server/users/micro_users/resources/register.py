import re

from werkzeug.security import generate_password_hash

from flask_restplus import Resource, Namespace, fields

from micro_users import db

from micro_users.models import BaseUser
from micro_users.schemas import user_schema

api = Namespace('')
register_user = api.model('RegisterUser', {'username': fields.String(required=True),
                                           'password': fields.String(required=True),
                                           'email': fields.String(required=True)})


@api.route('/register')
class Register(Resource):

    @staticmethod
    def add_user(data):
        user = BaseUser(
            username=data['username'],
            password=generate_password_hash(data['password']),
            email=data['email']
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def is_validated(data):
        if BaseUser.query.filter_by(username=data['username']).first() is not None:
            return False
        regex = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not regex.match(data['email']):
            return False
        return True

    @api.expect(register_user)
    def post(self):
        data = api.payload
        print(data)
        if not self.is_validated(data):
            return 'Wrong data', 400
        user = Register.add_user(data=data)
        return user_schema.jsonify(user)
