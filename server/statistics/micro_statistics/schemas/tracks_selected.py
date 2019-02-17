from micro_statistics import ma

from micro_statistics.models.track_selected_count import TrackSelectedCount

class TrackSelected(ma.ModelSchema):
    class Meta:
        model = TrackSelectedCount

track_selected = TrackSelected(many=True)
