# IMDB Movies Overview

The Movies API Django project is a comprehensive movie database management system developed using Django and Django REST framework. It provides a RESTful API for managing movie-related information, such as titles, genres, directors, and more.

# How to run 

1. Clone the repository and create a virtual environment: python -m venv imdb_env

2. Activate your virtual environment: source env/bin/activate 

3. Install all required packages: pip install -r requirements.txt

4. Run the migrations using the command:  python manage.py migrate  

5. Run the command: python manage.py runserver 

6. To load the data use the command: python manage.py load_movies_csv 

7. To make sure that everything went well use the automated tests: ./manage.py test  

Access the API at http://localhost:8000.


# How to use 

After run the api you will be able to access the endpoints and documentation. 

Endpoints: 

1. Retrieve a list of all movies: GET /movies/

2. Retrieve details of a specific movie: GET /movies/{id}/

3. Add a new movie to the database: POST /movies/

4. Update details of a specific movie: PUT /movies/{id}/

5. Updates details of an existing movie: PATCH /movies/{id}/

6. Delete a specific movie: DELETE /movies/{id}/


Example : http://127.0.0.1:8000/movies/?search=Maciste 

You can also order by the columns : date_published, reviews, votes 

Example : http://127.0.0.1:8000/movies/?ordering=reviews 
