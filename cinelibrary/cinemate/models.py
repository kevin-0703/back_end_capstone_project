from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    tmdb_id = models.PositiveIntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.title} - {self.user.username} ({self.rating})'