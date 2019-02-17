from flask_jwt_simple import get_jwt_identity

def resolve_jwt_identity(app):
    with app.app_context():
        if get_jwt_identity() is None:
            return 'default'
        return get_jwt_identity()
