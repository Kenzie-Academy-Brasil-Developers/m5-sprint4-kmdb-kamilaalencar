from asyncore import read
from rest_framework import serializers
from genres.serializers import GenreSerializer

from movies.models import Movie
from genres.models import Genre

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genre_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)

        for genre in genre_data:
            genre_obj, created = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre_obj)
        return movie