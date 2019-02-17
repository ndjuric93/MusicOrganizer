from micro_statistics import ma

from micro_statistics.models.genre_selected import GenreSelected

class GenreCount(ma.ModelSchema):
    class Meta:
        model = GenreSelected

genre_count = GenreCount(many=True)
