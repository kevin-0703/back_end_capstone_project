from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from unittest.mock import patch
from .models import Review, Movie

class OMDbAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)  # authenticate for endpoints requiring login

    @patch('cinemate.views.requests.get')
    def test_omdb_movies_endpoint(self, mock_get):
        # Mock OMDb response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "Search": [
                {"Title": "Mission Impossible", "Year": "1996", "imdbID": "tt0117060"},
            ],
            "Response": "True"
        }

        url = reverse('omdb-movies')
        response = self.client.get(url, {'q': 'mission impossible'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Title', response.json()[0])
        self.assertEqual(response.json()[0]['Title'], 'Mission Impossible')

    @patch('cinemate.serializers.requests.get')
    def test_review_movie_details(self, mock_get):
        # Create a review linked to a fake OMDb movie
        movie = Movie.objects.create(
            title="Mission Impossible",
            description="A spy movie",
            release_date="1996-05-22",
            created_at="1996-05-22T00:00"
        )

        review = Review.objects.create(
            movie=movie,
            user=self.user,
            rating=5,
            comment="Great movie!"
        )

        # Mock OMDb response for serializer
        mock_get.return_value.json.return_value = {
            "Title": "Mission Impossible",
            "Year": "1996",
            "imdbID": "tt0117060"
        }

        url = reverse('review-list')  # DRF router default for ReviewViewSet
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['movie_details']['Title'], "Mission Impossible")

    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())
