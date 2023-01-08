from django.shortcuts import render
from .models import Movies

# Create your views here.
def movie_list(req):
    movie_objects = Movies.objects.all()
    return render(req, 'newapp/movie_list.html', {'movie_objects': movie_objects})
