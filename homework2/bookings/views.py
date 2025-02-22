from django.shortcuts import render
from bookings.models import Movie, Seat, Booking

def index(request):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {"movies": movies})

def book(request, movie_id):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {"movies": movies})

def history(request):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {"movies": movies})
