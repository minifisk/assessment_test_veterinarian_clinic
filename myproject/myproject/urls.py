""" URLs main project """

# Core Django imports
from django.urls import include, path
from django.contrib import admin

# Third party imports

# App imports


# Redirect "" to rest_api URLS
# Admin URL
# Login for the browsable URL
urlpatterns = [
    path("", include("rest_api.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
