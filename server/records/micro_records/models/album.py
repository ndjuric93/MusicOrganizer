from micro_records import db

from micro_records.models.artist import Artist


class Album(db.Model):
    ''' Album model '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship(Artist)
    image = db.Column(db.LargeBinary)
