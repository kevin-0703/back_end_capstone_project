from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Movie, Review

# Create your tests here.
class MovieReviewAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="kevin", password="pass1234")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')


    def test_create_movie(self):
        res = self.client.post("/cinemate/movies/", {"title": "Inception", "description": "Dreams", "release_date": "2010-07-16"})
        self.assertEqual(res.status_code, 201)


    def test_create_review(self):
        movie = Movie.objects.create(title="Interstellar", description="Space", release_date="2014-11-07")
        res = self.client.post("/cinemate/reviews/", {"movie": movie.id, "rating": 5, "comment": "Amazing!"})
        self.assertEqual(res.status_code, 201)