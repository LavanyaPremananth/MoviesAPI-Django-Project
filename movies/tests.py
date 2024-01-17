# movies/tests.py

from django.test import TestCase
from django.test import Client
from .mocks import Mocks
from rest_framework import status

# URL for the movies endpoint
MOVIES_SET_URL = "/movies/"

class MoviesTests(TestCase):

    def setUp(self):
        # Set up test client and mocks for data creation
        self.client = Client()
        self.mocks = Mocks()

    def test_regular_get(self):
        """
        Test the regular GET request to retrieve all movies.
        """
        # Create movies
        self.mocks.create_movies()
        
        # Perform a GET request to retrieve all movies
        response = self.client.get(MOVIES_SET_URL)
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 5)

    def test_get_search_imdb_id(self):
        """
        Test GET request with search parameter for IMDb ID.
        """
        # Create movies
        self.mocks.create_movies()
        
        # Perform a GET request with search parameter for IMDb ID
        response = self.client.get(MOVIES_SET_URL + "?search=tt8764144")
        
        # Assertions
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Additional assertions for specific movie data

    def test_get_search_language(self):
        """
        Test GET request with search parameter for language.
        """
        # Create movies
        self.mocks.create_movies()
        
        # Perform a GET request with search parameter for language
        response = self.client.get(MOVIES_SET_URL + "?search=Ukraine")
        
        # Assertions
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Additional assertions for specific movie data

    def test_get_ordering_by_date(self):
        """
        Test GET request with ordering by date.
        """
        # Create movies
        self.mocks.create_movies()
        
        # Perform a GET request with ordering by date
        response = self.client.get(MOVIES_SET_URL + "?ordering=-date_published")
        
        # Assertions
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Additional assertions for specific movie data

    def test_post_request(self):
        """
        Test POST request to create a new movie.
        """
        # Given post_data for a new movie
        post_data = {
            # Movie data fields
        }

        # Perform a POST request to create a new movie
        response = self.client.post(MOVIES_SET_URL, post_data)

        # Assertions
        expected_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additional assertions for specific movie data

    def test_put_request(self):
        """
        Test PUT request to update an existing movie.
        """
        # Given put_data for an existing movie
        put_data = {
            # Updated movie data fields
        }

        # Perform a PUT request to update an existing movie
        response = self.client.put(MOVIES_SET_URL + str(movie_id) + "/", put_data, content_type='application/json')

        # Assertions
        expected_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Additional assertions for specific movie data

    def test_delete_request(self):
        """
        Test DELETE request to delete an existing movie.
        """
        # Given an existing movie's ID
        id_movie = self.mocks.create_movies()

        # Perform a DELETE request to delete the existing movie
        response = self.client.delete(MOVIES_SET_URL + str(id_movie["id"]) + "/")
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Perform a GET request to check if the movie is deleted
        response = self.client.get(MOVIES_SET_URL + str(id_movie["id"]) + "/")
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
