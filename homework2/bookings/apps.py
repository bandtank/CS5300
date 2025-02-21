from django.apps import AppConfig

# I don't know where this file came from. Perhaps it was automatically
# created after the first migration. Unfortunately, the documentation
# for Django is not clear about the origin of this file.
class BookingsConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'bookings'
