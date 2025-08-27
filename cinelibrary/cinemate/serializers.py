from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User

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
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']