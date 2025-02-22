from django.shortcuts import render
from bookings.models import Movie, Seat, Booking
from datetime import datetime, timedelta

def index(request):
  movies = Movie.objects.all()

  start_time = datetime.strptime("09:00", '%H:%M')
  end_time = datetime.strptime("23:00", '%H:%M')

  show_times = []
  current_time = start_time
  while current_time <= end_time:
    show_times.append(current_time.strftime('%H:%M'))
    current_time += timedelta(hours=3)

  return render(request, "movie_list.html", {"movies": movies, "show_times": show_times})

def book(request, movie_id, time):
  movie = Movie.objects.filter(id = movie_id).first()
  if movie is None:
    return render(request, "404-movie.html", {"movie_id": movie_id})

  seats = Seat.objects.all()
  return render(request, "seat_booking.html", {"movie": movie, "seats": seats})

def history(request):
  bookings = Booking.objects.all()
  return render(request, "booking_history.html", {"bookings": bookings})
