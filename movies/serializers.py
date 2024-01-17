# movies/serializers.py

from rest_framework.serializers import ModelSerializer
from .models import Movies

class MoviesSerializer(ModelSerializer):
    # Serializer for the Movies model

    class Meta:
        # Meta class to define the model and fields to be serialized
        model = Movies  # Specifies the model to be serialized
        fields = (
            "id", "imdb_id", "title", "original_title", "year",
            "genre", "duration", "country", "language",
            "votes", "budget", "reviews", "date_published"
        )
        # Specifies the fields of the model to be included in the serialized output
