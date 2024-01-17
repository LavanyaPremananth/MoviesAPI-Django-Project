# movies/views.py

from django.shortcuts import render

def index(request):
    # Your view logic goes here
    return render(request, 'index.html', {'msg': 'Welcome to the Movies App!'})
