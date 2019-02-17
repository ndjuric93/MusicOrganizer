from micro_records import db


class Artist(db.Model):
    ''' Artist model '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.LargeBinary)
