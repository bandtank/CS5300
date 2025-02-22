from rest_framework import viewsets, status
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.response import Response
from django.utils.timezone import make_aware
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

"""
The classes in this file represent the endpoints for the API. All
CRUD operations via REST are serviced by these classes. The Booking
class is the most complex because it must check for conflicts
between movie, seat, and showing time selections.
"""

class MovieViewSet(viewsets.ModelViewSet):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()

class SeatViewSet(viewsets.ModelViewSet):
  serializer_class = SeatSerializer
  queryset = Seat.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()

  def create(self, request):
    # Get the parameters in raw form
    booking_date_str = request.data.get('booking_date')
    movie_id = int(request.data.get('movie'))
    seat_id = int(request.data.get('seat'))

    # Try to make a timezone-aware datetime
    try:
      format_string = "%Y-%m-%dT%H:%M"
      booking_date_naive = datetime.strptime(booking_date_str, format_string)
      booking_date = make_aware(booking_date_naive)
    except:
      return Response(
        {"Error": f"Invalid value for booking_date: '{booking_date_str}'"},
        status = status.HTTP_400_BAD_REQUEST,
      )

    # See if this booking conflicts with other bookings
    booking = Booking.objects.filter(movie_id = movie_id, seat_id = seat_id, booking_date = booking_date)
    if booking:
      return Response(
        {"Error": f"Duplicate booking for seat_id = {seat_id}, movie_id = {movie_id}, booking_date = {booking_date}"},
        status = status.HTTP_400_BAD_REQUEST,
      )

    # Create the new booking
    seat = Seat.objects.filter(id = seat_id).first()
    movie = Movie.objects.filter(id = movie_id).first()
    booking = Booking.objects.create(movie = movie, seat = seat, booking_date = booking_date)

    return Response(
      BookingSerializer(booking).data,
      status = status.HTTP_201_CREATED
    )