# pylint: disable=too-many-ancestors
""" Views """

# Django core imports
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


# Third party imports
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# App imports
from .serializers import UserSerializer, GroupSerializer, HeroSerializer
from .models import Hero

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API viewset endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API viewset endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HeroViewSet(viewsets.ModelViewSet):
    """
    API viewset endpoint for viewing and editing heroes
    """

    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializer


class HeroApiView(APIView):
    """
    API view for heroes
    """

    permission_classes = []

    def get(self, request):
        """
        Return a list of all Heroes
        """

        ### PERFORM LOGIC
        heroes_queryset = Hero.objects.all().order_by("name")
        serialized_heroes = HeroSerializer(heroes_queryset, many=True)
        return Response(serialized_heroes.data)
