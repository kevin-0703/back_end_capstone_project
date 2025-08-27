from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tmdb import search_movies, get_movie_details

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(["GET"])
def search_tmdb_movies(request):
    query = request.GET.get("q")
    if not query:
        return Response({"error": "Missing query"}, status=400)
    results = search_movies(query)
    return Response(results)

@api_view(["GET"])
def movie_details_tmdb(request, movie_id):
    details = get_movie_details(movie_id)
    if details:
        return Response(details)
    return Response({"error": "Movie not found"}, status=404)


@api_view(["POST"])
def add_movie_from_tmdb(request):
    tmdb_id = request.data.get("tmdb_id")
    if not tmdb_id:
        return Response({"error": "tmdb_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if already exists
    if Movie.objects.filter(tmdb_id=tmdb_id).exists():
        return Response({"error": "Movie already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch from TMDB
    details = get_movie_details(tmdb_id)
    if not details:
        return Response({"error": "Movie not found on TMDB"}, status=status.HTTP_404_NOT_FOUND)

    movie = Movie.objects.create(
        title=details.get("title"),
        description=details.get("overview"),
        release_date=details.get("release_date") or None,
        poster_url=f"https://image.tmdb.org/t/p/w500{details['poster_path']}" if details.get("poster_path") else None,
        tmdb_id=tmdb_id
    )

    return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)