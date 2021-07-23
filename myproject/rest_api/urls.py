""" URLs rest_api app """

# Core Django imports
from django.urls import include, path

# Third party imports
from rest_framework import routers

# App imports
from rest_api import views


# Register users, groups and heroes-enpoints with the router
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"heroes", views.HeroViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
    path("heroesAPI/", views.HeroApiView.as_view(), name="Heroes API"),
]
