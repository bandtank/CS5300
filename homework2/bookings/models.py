from django.db import models

# Create your models here.
class Movie(models.Model):
  title = models.CharField()
  description = models.TextField()
  release_date = models.DateField()
  duration = models.IntegerField()

class Seat(models.Model):
  seat_number = models.CharField()
  is_booked = models.BooleanField()

class Booking(models.Model):
  # FIXME: on_delete for all FKs
  #   Options: Cascade, protect, restrict, set_null, set_default, , set(), do_nothing
  # FIXME: add FKs to other classes?
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  booking_date = models.DateTmeField()