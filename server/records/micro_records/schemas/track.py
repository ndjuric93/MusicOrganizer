from micro_records import ma

from micro_records.models import Track

from micro_utils.marshmallow.leading_zeros_integer_field import LeadingZerosIntegerField



class TrackSchema(ma.ModelSchema):
    track_number = LeadingZerosIntegerField(zeros_count=1)

    class Meta:
        model = Track

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)
