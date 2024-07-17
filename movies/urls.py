from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreate.as_view(), name='get_all_movies'),
    path('movies/detail/', views.MovieDetailView.as_view(), name='get_movie_detail'),
    path('movies/watchlist/', views.WatchlistListCreate.as_view(), name='get_watchlist'),
]