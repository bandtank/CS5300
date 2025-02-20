from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Attach the bookings app at the root url
    path('', include("bookings.urls")),
]
