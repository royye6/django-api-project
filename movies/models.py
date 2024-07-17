from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True, null=True)
    poster_path = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s watchlist - {self.movie.title}"

    class Meta:
        unique_together = ['user', 'movie']

