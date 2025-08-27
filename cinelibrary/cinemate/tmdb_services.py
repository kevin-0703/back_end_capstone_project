import requests
from django.conf import settings

TMDB_BASE_URL = "https://api.themoviedb.org/3"

def get_movie_details(movie_id):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}"
    params = {"api_key": settings.TMDB_API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def search_movies(query):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {"api_key": settings.TMDB_API_KEY, "query": query, "language": "en-US"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
