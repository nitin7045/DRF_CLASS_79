from django.shortcuts import render
from myappone.models import Movie
from django.http import HttpResponse

# Create your views here.

# --------------------------------------------------------------------------------------------
def movie_list(request):
    movies = Movie.objects.all()
    return HttpResponse(list(movies.values()))