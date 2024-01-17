# movies/models.py

from django.db import models

class Movies(models.Model):
    # Model representing a movie with various attributes

    # IMDb ID of the movie (e.g., "tt8764144")
    imdb_id = models.CharField(max_length=50) 

    # Title of the movie (e.g., "A Wakefield Project")
    title = models.CharField(max_length=100, null=True, blank=True)

    # Original title of the movie (e.g., "A Wakefield Project")
    original_title = models.CharField(max_length=100, null=True, blank=True)

    # Year of the movie (e.g., "2019")
    year = models.CharField(max_length=10, null=True, blank=True)

    # Date when the movie was published
    date_published = models.DateField(null=True, blank=True)

    # Genre of the movie (e.g., "Horror, Sci-Fi, Thriller")
    genre = models.CharField(max_length=100, null=True, blank=True)

    # Duration of the movie (e.g., "88" minutes)
    duration = models.CharField(max_length=100, null=True, blank=True)

    # Country of origin of the movie (e.g., "Canada, USA")
    country = models.CharField(max_length=100, null=True, blank=True)

    # Language of the movie (e.g., "English")
    language = models.CharField(max_length=50, null=True, blank=True)

    # Director of the movie (e.g., "John Doe")
    director = models.CharField(max_length=50, null=True, blank=True)

    # Number of votes the movie has received
    votes = models.IntegerField(null=True, blank=True)

    # Budget of the movie (e.g., "$500.000")
    budget = models.CharField(max_length=50)

    # Reviews/ratings of the movie (e.g., 12.0)
    reviews = models.FloatField(null=True, blank=True)
