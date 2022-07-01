from dataclasses import fields
from rest_framework import serializers
from .models import Review
from users.models import User
from movies.models import Movie

class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    stars = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model= Review
        fields = ['id', 'stars', 'review', 'spoilers',  'movie_id', 'critic', 'recomendation']
        extra_kwargs = {'recomendation': {'required': False}, 'movie': {'required': False}, 'critic':{'required': False}}
    
    def create(self, validated_data:dict):
        return Review.objects.create( **validated_data)
        