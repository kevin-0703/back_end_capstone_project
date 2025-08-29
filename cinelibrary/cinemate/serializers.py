from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User
import requests

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    movie_details = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'movie_imdb_id', 'movie_details', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']
    def get_movie_details(self, obj):
        OMDB_API_KEY = "bc92eef9"
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={obj.movie_imdb_id}"
        r = requests.get(url).json()
        return r