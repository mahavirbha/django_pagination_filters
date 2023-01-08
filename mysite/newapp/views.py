from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.
def movie_list(req):
    movie_objects = Movies.objects.all()

    paginator = Paginator(movie_objects,3)
    page = req.GET.get('page')
    movie_objects = paginator.get_page(page)

    return render(req, 'newapp/movie_list.html', {'movie_objects': movie_objects})
