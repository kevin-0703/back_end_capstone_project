from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MovieViewSet, ReviewViewSet, RegisterView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
urlpatterns = [
    path('cinemate/', include(router.urls)),
    path('cinemate/register/', RegisterView.as_view(), name='register'),
    path("tmdb/search/", views.search_tmdb_movies, name="search_tmdb_movies"),
    path("tmdb/movie/<int:movie_id>/", views.movie_details_tmdb, name="movie_details_tmdb"),
    path("movies/add/", views.add_movie_from_tmdb, name="add_movie_from_tmdb"),
]