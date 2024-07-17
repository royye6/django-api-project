from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import MovieSerializer, WatchlistSerializer
from .models import Movie, Watchlist
import requests
import os


TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_BASE_URL = os.environ.get('TMDB_BASE_URL')
SEARCH_TERM = ''

"""
Search input required to integrate external API 
Modify when templates are created
"""

class MovieDetailView(APIView):
    def get(self, request, tmdb_id):
        url = f"{TMDB_BASE_URL}query={SEARCH_TERM}&api_key={TMDB_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            movie, created = Movie.objects.get_or_create(tmdb_id=tmdb_id)
            movie.title = data.get('title')
            movie.overview = data.get('overview')
            movie.release_date = data.get('release_date')
            movie.poster_path = data.get('poster_path')
            movie.save()
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MovieListCreate(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class WatchlistListCreate(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
