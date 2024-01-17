# movies/urls.py

from django.contrib import admin
from django.urls import path
from rest_framework import routers
from movies.view_sets import MoviesViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create a schema view for Swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Movies API",
      default_version='v1',
      description="Movies database from imdb. Use /movies/ end point to access the data",
      contact=openapi.Contact(email="premanan001@mymail.sim.edu.sg"),
   ),
   public=True,
)

# Create a router for registering the MoviesViewSet
router = routers.SimpleRouter()
router.register(r'movies', MoviesViewSet)

# Define urlpatterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),  # Swagger documentation URL
]

# Include the URLs from the router (registering MoviesViewSet)
urlpatterns += router.urls
