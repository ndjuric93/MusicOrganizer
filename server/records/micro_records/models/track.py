from micro_records import db

from micro_records.models.album import Album


class Track(db.Model):
    ''' Track model '''
    id = db.Column(db.Integer, primary_key=True)
    track_number = db.Column(db.Integer)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    path = db.Column(db.String)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    album = db.relationship(Album)
