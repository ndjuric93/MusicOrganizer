from marshmallow import fields
from micro_records import ma

from micro_records.models import Album
from micro_records.schemas import ArtistSchema, TrackSchema


class AlbumSchema(ma.ModelSchema):
    artist = fields.Nested(ArtistSchema)
    tracks = fields.Nested(TrackSchema, many=True)

    class Meta:
        model = Album


albums_schema = AlbumSchema(many=True)
