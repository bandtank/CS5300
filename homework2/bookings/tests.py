from django.test import TestCase
from django.utils.timezone import make_aware
from bookings.models import Movie, Seat, Booking
from datetime import datetime
from rest_framework.test import APIClient
from rest_framework import status
import logging

def get_aware_date(date_string):
  format_string = "%Y-%m-%dT%H:%M"
  booking_date_naive = datetime.strptime(date_string, format_string)

  return make_aware(booking_date_naive)

###
# Test the models: Movie, Seat, Booking
#
# This class calls internal methods from within the application.
###
class ModelTests(TestCase):
  def setUp(self):
    self.booking_date = get_aware_date("2025-06-30T15:00")

    self.movie = Movie.objects.create(
      title = "Test Movie 123",
      description = "This is a test movie.",
      release_date = "2025-01-01",
      duration = 100,
    )

    self.seat = Seat.objects.create(
      seat_number = 120,
      is_booked=False
    )

    self.booking = Booking.objects.create(
      movie = self.movie,
      seat = self.seat,
      booking_date = self.booking_date,
    )



    ##########
    ## Movies
    ###
  def test_find_a_movie(self):
    # Check to see if the class's test movie exists
    movie = Movie.objects.filter(
      title = "Test Movie 123",
    ).first()

    self.assertFalse(movie is None)

  def test_create_a_movie(self):
    title = "New Movie"
    description = "Test Description"
    release_date = "2020-01-01"
    duration = 120

    # The test movie should not exist yet
    movie = Movie.objects.filter(
      title = title,
      description = description,
      release_date = release_date,
      duration = duration
    ).first()

    self.assertTrue(movie is None)

    # Create the movie and then check for it to exist
    movie = Movie.objects.create(
      title = title,
      description = description,
      release_date = release_date,
      duration = duration
    )
    movie = Movie.objects.filter(
      title = title,
      description = description,
      release_date = release_date,
      duration = duration
    ).first()

    self.assertFalse(movie is None)

  def test_update_a_movie(self):
    movie = Movie.objects.filter(
      title = "Test Movie 123",
    ).first()
    self.assertFalse(movie is None)

    movie.title = "New Title"
    movie.save()

    movie = Movie.objects.filter(
      title = "Test Movie 123",
    ).first()
    self.assertTrue(movie is None)

    movie = Movie.objects.filter(
      title = "New Title",
    ).first()
    self.assertFalse(movie is None)

  def test_delete_a_movie(self):
    movie = Movie.objects.filter(
      title = "Test Movie 123",
    ).first()
    self.assertFalse(movie is None)

    movie_count = Movie.objects.count()
    movie.delete()
    self.assertEqual(Movie.objects.count(), movie_count - 1)

  ##########
  ## Seats
  ###
  def test_find_a_seat(self):
    # Check to see if the class's test seat exists
    seat = Seat.objects.filter(
      seat_number = 120,
    ).first()

    self.assertFalse(seat is None)

  def test_create_a_seat(self):
    seat_number = 130
    is_booked = False

    # The test seat should not exist yet
    seat = Seat.objects.filter(
      seat_number = 130,
      is_booked = False,
    ).first()

    self.assertTrue(seat is None)

    # Create the seat and then check for it to exist
    seat = Seat.objects.create(
      seat_number = 130,
      is_booked = False,
    )

    seat = Seat.objects.filter(
      seat_number = 130,
      is_booked = False,
    ).first()

    self.assertFalse(seat is None)

  def test_update_a_seat(self):
    seat = Seat.objects.filter(
      seat_number = 120
    ).first()
    self.assertFalse(seat is None)

    seat.seat_number = 150
    seat.save()

    seat = Seat.objects.filter(
      seat_number = 120
    ).first()
    self.assertTrue(seat is None)

    seat = Seat.objects.filter(
      seat_number = 150
    ).first()
    self.assertFalse(seat is None)

  def test_delete_a_seat(self):
    seat = Seat.objects.filter(
      seat_number = 120
    ).first()
    self.assertFalse(seat is None)

    seat_count = Seat.objects.count()
    seat.delete()
    self.assertEqual(Seat.objects.count(), seat_count - 1)

  ##########
  ## Bookings
  ###
  def test_find_a_booking(self):
    # Check to see if the class's test booking exists
    booking = Booking.objects.filter(
      movie_id = self.movie.id,
      seat_id = self.seat.id,
      booking_date = self.booking_date,
    ).first()

    self.assertFalse(booking is None)

  def test_create_a_booking(self):
    booking_date = get_aware_date("1999-06-30T15:00")

    # The test booking should not exist yet
    booking = Booking.objects.filter(
      booking_date = booking_date,
    ).first()

    self.assertTrue(booking is None)

    # Create the booking and then check for it to exist
    booking = Booking.objects.create(
      movie = self.movie,
      seat = self.seat,
      booking_date = booking_date,
    )

    booking = Booking.objects.filter(
      booking_date = booking_date,
    ).first()

    self.assertFalse(booking is None)

  def test_update_a_booking(self):
    booking = Booking.objects.filter(
      booking_date = self.booking_date,
    ).first()
    self.assertFalse(booking is None)

    new_booking_date = get_aware_date("2999-06-30T15:00")

    booking.booking_date = new_booking_date
    booking.save()

    booking = Booking.objects.filter(
      booking_date = self.booking_date,
    ).first()
    self.assertTrue(booking is None)

    booking = Booking.objects.filter(
      booking_date = new_booking_date,
    ).first()
    self.assertFalse(booking is None)

  def test_delete_a_booking(self):
    booking = Booking.objects.filter(
      booking_date = self.booking_date,
    ).first()
    self.assertFalse(booking is None)

    booking_count = Booking.objects.count()
    booking.delete()
    self.assertEqual(Booking.objects.count(), booking_count - 1)


###
# Test the API: Movie, Seat, Booking
#
# This class uses the APIClient module to make calls
# to the REST endpoints.
###
class APITests(TestCase):
  def setUp(self):
    self.api_client = APIClient()

    self.booking_date_string = "2025-06-30T15:00"
    self.booking_date = get_aware_date(self.booking_date_string)

    self.movie = Movie.objects.create(
      title = "Test Movie 123",
      description = "This is a test movie.",
      release_date = "2025-01-01",
      duration = 100,
    )

    self.seat = Seat.objects.create(
      seat_number = 120,
      is_booked=False
    )

    self.booking = Booking.objects.create(
      movie = self.movie,
      seat = self.seat,
      booking_date = self.booking_date,
    )

    """Reduce the log level to avoid messages like 'Bad Request'"""
    logger = logging.getLogger("django.request")
    self.previous_level = logger.getEffectiveLevel()
    logger.setLevel(logging.ERROR)

  def tearDown(self):
    """Reset the log level back to normal"""
    logger = logging.getLogger("django.request")
    logger.setLevel(self.previous_level)

  ##########
  ## /api/movies/
  ###
  def test_get_movie_list(self):
    # Get the test movie
    result = self.api_client.get(f"/api/movies/{self.movie.id}/")
    self.assertEqual(len(result.data), 7)

     # Get all movies
    result = self.api_client.get(f"/api/movies/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_create_movie(self):
    # Create a new test movie
    result = self.client.post("/api/movies/", {
      "title": "New Movie 123", 
      "description": "Test Description", 
      "release_date": "2021-01-01",
      "duration": 60,
    })

    self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    # Use the API to get the test movie
    result = self.api_client.get(f"/api/movies/{result.data['id']}/")
    self.assertEqual(len(result.data), 7)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_delete_movie(self):
    # Check to be sure a movie exists
    result = self.api_client.get("/api/movies/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Delete the movie
    result = self.client.delete(f"/api/movies/{self.movie.id}/")
    self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    # Check to be sure it has been deleted
    result = self.api_client.get("/api/movies/")
    self.assertEqual(len(result.data), 0)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_movie_update_api(self):
    # Get the test movie
    result = self.api_client.get(f"/api/movies/{self.movie.id}/")
    self.assertEqual(len(result.data), 7)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Update the test movie
    result = self.client.patch(f"/api/movies/{result.data['id']}/", {
      "title": 'A New Title',
      "description": "A New Description",
      "release_date": "2019-01-01",
      "duration": 99,
    }, format='json', content_type="application/json")
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Check to be sure the fields have been updated
    result = self.api_client.get(f"/api/movies/{self.movie.id}/")
    self.assertEqual(len(result.data), 7)
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    self.assertEqual(result.data["title"], "A New Title")
    self.assertEqual(result.data["description"], "A New Description")
    self.assertEqual(result.data["release_date"], "2019-01-01"),
    self.assertEqual(result.data["duration"], 99)

  ##########
  ## /api/seats/
  ###
  def test_get_seat_list(self):
    # Get the test seat
    result = self.api_client.get("/api/seats/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_create_seat(self):
    # Create a new test seat
    result = self.client.post("/api/seats/", {
      "seat_number": 123,
    })

    self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    # Use the API to get the test seat
    result = self.api_client.get(f"/api/seats/{result.data['id']}/")
    self.assertEqual(len(result.data), 3)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_delete_seat(self):
    result = self.api_client.get("/api/seats/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    result = self.client.delete(f"/api/seats/{self.seat.id}/")
    self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    result = self.api_client.get("/api/seats/")
    self.assertEqual(len(result.data), 0)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_update_seat(self):
    # Get the test seat
    result = self.api_client.get(f"/api/seats/{self.seat.id}/")
    self.assertEqual(len(result.data), 3)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Update the test seat
    result = self.client.patch(f"/api/seats/{result.data['id']}/", {
      "seat_number": 201,
      "is_booked": 1,
    }, format='json', content_type="application/json")
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Check to be sure the fields have been updated
    result = self.api_client.get(f"/api/seats/{self.seat.id}/")
    self.assertEqual(len(result.data), 3)
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    self.assertEqual(result.data["seat_number"], "201")
    self.assertEqual(result.data["is_booked"], True)

  ##########
  ## /api/bookings/
  ###
  def test_get_booking_list(self):
    result = self.api_client.get("/api/bookings/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_create_booking(self):
    # Create a new test seat
    result = self.client.post("/api/bookings/", {
      "movie": self.movie.id,
      "seat": self.seat.id,
      "booking_date": "2021-01-01T12:34"
    })

    self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    # Use the API to get the test seat
    result = self.api_client.get(f"/api/bookings/{result.data['id']}/")
    self.assertEqual(len(result.data), 4)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_create_duplicate_booking(self):
    # Create a new test seat
    result = self.client.post("/api/bookings/", {
      "movie": self.movie.id,
      "seat": self.seat.id,
      "booking_date": "2021-01-01T12:34"
    })

    self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    result = self.client.post("/api/bookings/", {
      "movie": self.movie.id,
      "seat": self.seat.id,
      "booking_date": "2021-01-01T12:34"
    })
    self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.data['Error'],
    'Duplicate booking for seat_id = 1, movie_id = 1, booking_date = 2021-01-01 12:34:00-07:00')

  def test_delete_booking(self):
    result = self.api_client.get("/api/bookings/")
    self.assertEqual(len(result.data), 1)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    result = self.client.delete(f"/api/bookings/{self.booking.id}/")
    self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    result = self.api_client.get("/api/bookings/")
    self.assertEqual(len(result.data), 0)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

  def test_update_booking(self):
    # Get the test booking
    result = self.api_client.get(f"/api/bookings/{self.booking.id}/")
    self.assertEqual(len(result.data), 4)
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Update the test booking
    result = self.client.patch(f"/api/bookings/{result.data['id']}/", {
      "booking_date": "2011-01-01T23:48",
    }, format='json', content_type="application/json")
    self.assertEqual(result.status_code, status.HTTP_200_OK)

    # Check to be sure the fields have been updated
    result = self.api_client.get(f"/api/bookings/{self.seat.id}/")
    self.assertEqual(len(result.data), 4)
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    self.assertEqual(result.data["booking_date"], "2011-01-01T23:48:00-07:00")