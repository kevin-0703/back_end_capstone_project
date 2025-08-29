from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests

OMDB_API_KEY = " bc92eef9"
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OMDbMovieListView(APIView):
    def get(self, request):
        omdb_api_key = "bc92eef9"
        query = request.GET.get("q", "mission impossible")
        url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&s={query}"
        response = requests.get(url)
        data = response.json()
        return Response(data)