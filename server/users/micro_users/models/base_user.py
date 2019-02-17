from werkzeug.security import check_password_hash

from micro_users import db


class BaseUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False, )

    def check_password(self, password):
        return check_password_hash(pwhash=self.password, password=password)
