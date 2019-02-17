from micro_statistics import ma

from micro_statistics.models.track_played_count import TrackPlayedCount

class TrackPlayed(ma.ModelSchema):
    class Meta:
        model = TrackPlayedCount

track_played = TrackPlayed(many=True)
