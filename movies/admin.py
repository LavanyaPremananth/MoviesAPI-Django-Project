# movies/admin.py

from django.contrib import admin
from .models import Movies  # Import the Movies model from the same app

# Register the Movies model with the Django admin site
admin.site.register(Movies)
