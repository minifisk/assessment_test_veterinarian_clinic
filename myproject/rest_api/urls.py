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
        views.AppointmentView.as_view(),
        name="Appointment View",
    ),
]
