from flask_restplus import Resource, Namespace, fields
from flask_jwt_simple import create_jwt

from micro_users.models import BaseUser

api = Namespace('')
login_user = api.model('User', {'username': fields.String(required=True),
                                'password': fields.String(required=True)})


@api.route('/login')
class Login(Resource):

    @api.expect(login_user)
    def post(self):
        data = api.payload
        print(data)
        user = BaseUser.query.filter_by(username=data['username']).first()
        # publish jwt ?
        if user is not None and user.check_password(data['password']):
            return {
                'token': create_jwt(identity=user.id)
            }
        return 'AccessDenied', 400
