import django.db.models as models

class Movie(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField(max_length = 500)
  release_date = models.DateField()
  duration = models.IntegerField()

class Seat(models.Model):
  seat_number = models.CharField(max_length = 30)
  is_booked = models.BooleanField(default = False)

class Booking(models.Model):
  # Delete the booking if the movie has been deleted
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  # Delete the booking if the seat has been deleted 
  seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

  #
  booking_date = models.DateTimeField(blank = True, null = True)