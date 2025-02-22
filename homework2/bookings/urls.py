from django.urls import path, include
from rest_framework.routers import SimpleRouter
from bookings.views import index, book, history
from bookings.api import MovieViewSet, SeatViewSet, BookingViewSet
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
  path("", index, name = "index"),
  path("book/<int:movie_id>/<str:time>/", book, name = "book"),
  path("history/", history, name = "history"),
  path('api/', include(router.urls)),
]

urlpatterns += static(
  settings.MEDIA_URL,
  document_root=settings.MEDIA_ROOT
)