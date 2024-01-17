# asgi.py

"""
ASGI config for movies_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to 'movies_api.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_api.settings')

# Get the ASGI application using Django's get_asgi_application function
application = get_asgi_application()
