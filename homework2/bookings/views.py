from django.shortcuts import render
from django.utils import timezone
from bookings.models import Movie, Seat, Booking
from datetime import datetime, timedelta, date
import math
import logging

logger = logging.getLogger(__name__)

def index(request):
  movies = Movie.objects.all()
  days = get_showing_days_times()
  return render(request, "movie_list.html", {"movies": movies, "days": days})

def get_showing_days_times():
  today = timezone.localtime()
  days = []
  for i in range(3):
    date = today + timedelta(days = i)

    if i == 0:
      display = "Today"
    elif i == 1:
      display = "Tomorrow"
    else:
      display = date.strftime("%A")
    
    times = []
    if i == 0:
      for hour in range(math.ceil(today.hour / 3) * 3, 24, 3):
        times.append(f"{hour:02d}:00")
    else:
      for hour in range(9, 24, 3):
        times.append(f"{hour:02d}:00")

    days.append({
      "display": display,
      "date": date.strftime("%Y-%m-%d"),
      "times": times,
    })

  return days

def book(request, movie_id, date, time):
  movie = Movie.objects.filter(id = movie_id).first()
  if movie is None:
    return render(request, "404-movie.html", {"movie_id": movie_id})
  
  # Using the date and time, find the bookings for this showing

  bookings = Booking.objects.all()
  seats = Seat.objects.all()

  date = datetime.strptime(date, "%Y-%m-%d")

  return render(request, "seat_booking.html", {
    "movie": movie,
    "date": date.strftime("%A, %B %d "),
    "time": time,
    "seats": seats,
  })

def history(request):
  bookings = Booking.objects.all()
  return render(request, "booking_history.html", {"bookings": bookings})
