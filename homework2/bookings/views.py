from django.shortcuts import render, redirect
from django.utils import timezone
from bookings.models import Movie, Seat, Booking
from datetime import datetime, timedelta, date
import math
import logging

logger = logging.getLogger(__name__)

def index(request):
  """
  This is the default entry point of the application.
  It renders a list of movies for the user to view.
  """

  movies = Movie.objects.all()
  days = get_showing_days_times()
  return render(request, "movie_list.html", {"movies": movies, "days": days})

def get_showing_days_times():
  """
  This function creates a list of days and times for movies to
  be viewed in the near future. It does not include times that
  are already in the past.
  """

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
  """
  This function allows a user to book a showing. If the function is called
  from the index, the rendered page will ask the user to select a seat. If
  the function is called by the submission of a form, a booking will be
  created, presuming no errors are encountered.
  """

  # Find the movie first
  movie = Movie.objects.filter(id = movie_id).first()
  if movie is None:
    return render(request, "404-movie.html", {"movie_id": movie_id})
  
  # Get the date from the caller and make sure it is in the right timezone
  booking_date_naive = datetime.strptime(date, "%Y-%m-%d")
  tz = timezone.get_current_timezone()
  booking_date = timezone.make_aware(booking_date_naive, tz)

  # Using the selected time, find the bookings for the showing
  time_components = time.split(":")
  booking_date = booking_date.replace(
    hour = int(time_components[0]),
    minute = int(time_components[1])
  )

  bookings = Booking.objects.filter(movie_id = movie.id, booking_date = booking_date)
  taken_seats = [booking.seat_id for booking in bookings]

  # Do not allow booked seats to be selected
  seats = Seat.objects.exclude(id__in = taken_seats)

  # Create the booking
  if request.method == "POST":
    seat_id = int(request.POST.get("seat_id"))
    if seat_id in taken_seats:
      return render(request, "404-seat-taken.html", {"seat_id": seat_id})

    seat = Seat.objects.filter(id = seat_id).first()
    if seat is None:
      return render(request, "404-unknown-seat.html", {"seat_id": seat_id})
    
    Booking.objects.create(movie = movie, seat = seat, booking_date = booking_date)

    return redirect('history')

  # Show the booking information to confirm seat selection
  else:
    return render(request, "seat_booking.html", {
      "movie": movie,
      "date": booking_date.strftime("%A, %B %d "),
      "time": time,
      "seats": seats,
    })

def history(request):
  """
  This function renders a historical view of bookings as related to the user.
  """

  bookings = Booking.objects.all()

  history = []
  for booking in bookings:
    movie = Movie.objects.filter(id = booking.movie_id).first()
    seat = Seat.objects.filter(id = booking.seat_id).first()

    history.append({
      "movie": movie.title,
      "seat": seat.seat_number,
      "date": booking.booking_date,
    })

  return render(request, "booking_history.html", {"bookings": history})