from django.core.management.base import BaseCommand
from movies.models import Movies
from datetime import datetime
import csv

# Define column indices for the CSV file
IMDB_ID = 0
TITLE = 1
ORIGINAL_TITLE = 2
YEAR = 3
DATE_PUBLISHED = 4
GENRE = 5
DURATION = 6
COUNTRY = 7
LANGUAGE = 8
DIRECTOR = 9
VOTES = 15
BUDGET = 16
REVIEWS = 20

class Command(BaseCommand):
    help = "Load the movies CSV file"

    def handle(self, *args, **kwargs):
        # List to hold Movie objects for bulk insertion
        insert_list = []

        # Clear existing data in the Movies model
        Movies.objects.all().delete()

        # Open the CSV file for reading
        with open("movies/management/commands/IMDb_movies.csv", encoding='utf-8') as csv_file:
            # Create a CSV reader
            csv_reader = csv.reader(csv_file, delimiter=',')
            count = 0

            # Iterate through each row in the CSV
            for row in csv_reader:
                if count != 0:  # Skip the header row
                    # Create a Movies object for each row in the CSV
                    movies = Movies()
                    movies.imdb_id = row[IMDB_ID]
                    movies.title = row[TITLE]
                    movies.original_title = row[ORIGINAL_TITLE]
                    movies.year = row[YEAR]

                    try:
                        # Handle date conversion
                        if "TV Movie" in row[DATE_PUBLISHED]:
                            movies.date_published = None  # or set to a default date
                        else:
                            if len(row[DATE_PUBLISHED]) == 4:
                                movies.date_published = datetime.strptime(row[DATE_PUBLISHED], '%Y')
                            else:
                                movies.date_published = datetime.strptime(row[DATE_PUBLISHED], '%Y-%m-%d')
                    except ValueError:
                        print(f"Not able to convert date: {row[DATE_PUBLISHED]}")
                        movies.date_published = None  # Handle the error or continue with a default value

                    movies.genre = row[GENRE]
                    movies.duration = row[DURATION]
                    movies.country = row[COUNTRY]
                    movies.language = row[LANGUAGE]
                    movies.votes = row[VOTES]
                    movies.budget = row[BUDGET]
                    
                    if row[REVIEWS]:
                        movies.reviews = row[REVIEWS]

                    # Add the Movies object to the insert list
                    insert_list.append(movies)
                count += 1  # Increment the row count

        # Bulk insert the Movies objects into the database
        Movies.objects.bulk_create(insert_list, batch_size=500)
