from micro_records import ma

from micro_records.models import Artist


class ArtistSchema(ma.ModelSchema):
    class Meta:
        model = Artist


artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)
