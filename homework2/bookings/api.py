from rest_framework import viewsets
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()

class SeatViewSet(viewsets.ModelViewSet):
  serializer_class = SeatSerializer
  queryset = Seat.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()

  # figure out if the seat has already been reserved for a particular showing
  # if yes, return error
  # if no, allow booking to be created
