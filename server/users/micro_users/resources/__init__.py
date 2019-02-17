from flask_restplus import Api

from .login import api as login
from .register import api as register
from .users import api as users

api = Api(title='Users')
api.add_namespace(login)
api.add_namespace(register)
api.add_namespace(users)
