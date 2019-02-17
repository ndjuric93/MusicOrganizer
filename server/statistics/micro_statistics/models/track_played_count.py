from micro_statistics import db

class TrackPlayedCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
