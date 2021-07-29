""" URLs rest_api app """

# Core Django imports
from django.urls import include, path

# Third party imports
from rest_framework import routers

# App imports
from rest_api import views


# Register users, groups and heroes-enpoints with the router
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "bookings/<str:physician_first_name>/<str:physician_last_name>/<str:date>",
        views.AppointmentDateView.as_view(),
        name="See all bookings for a physician at a specific date",
    ),
    path(
        "bookings/<str:physician_first_name>/<str:physician_last_name>/",
        views.PhysicianBookings.as_view(),
        name="See all bookings for a physician/Create new booking",
    ),
    path("bookings/", views.Booking, name="Booking form view")
]
