# wsgi.py

"""
WSGI config for movies_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_api.settings')

# Get the WSGI application for the Django project
application = get_wsgi_application()
