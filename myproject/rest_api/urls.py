""" URLs rest_api app """

# Core Django imports
from django.urls import include, path

# Third party imports
from rest_framework import routers

# App imports
from rest_api import views



# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", views.Index, name="index"),
    path(
        "bookings/<str:physician_first_name>/<str:physician_last_name>/<str:date>",
        views.AppointmentDateView.as_view(),
        name="datebookings",
    ),
    path(
        "bookings/<str:physician_first_name>/<str:physician_last_name>/",
        views.PhysicianBookings.as_view(),
        name="allbookings",
    ),
    path("bookings/", views.Booking, name="bookingsform")
]
