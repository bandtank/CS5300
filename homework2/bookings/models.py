import django.db.models as models

class Movie(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField(max_length = 500)
  release_date = models.DateField()
  duration = models.IntegerField()
  image = models.ImageField(upload_to = "movies/", null = True)
  rating = models.TextField(max_length = 10, null = True)

class Seat(models.Model):
  seat_number = models.CharField(max_length = 30)
  is_booked = models.BooleanField(default = False)

class Booking(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
  booking_date = models.DateTimeField(blank = True, null = True)