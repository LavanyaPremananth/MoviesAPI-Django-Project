# movies/view_sets.py

from rest_framework.viewsets import ModelViewSet
from .serializers import MoviesSerializer
from .models import Movies
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MoviesViewSet(ModelViewSet):
    # View set for handling CRUD operations on Movies model

    queryset = Movies.objects.all()  # Queryset containing all movies
    serializer_class = MoviesSerializer  # Serializer class for the Movies model
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # Define filter backends including DjangoFilterBackend, OrderingFilter, and SearchFilter

    ordering_fields = ["date_published", "reviews", "votes"]
    # Specify fields for ordering: date_published, reviews, votes

    search_fields = ["imdb_id", "title", "genre", "duration", "country", "language", "date_published"]
    # Specify fields for searching: imdb_id, title, genre, duration, country, language, date_published
