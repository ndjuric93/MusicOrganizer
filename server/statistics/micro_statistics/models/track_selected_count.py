from micro_statistics import db

class TrackSelectedCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
