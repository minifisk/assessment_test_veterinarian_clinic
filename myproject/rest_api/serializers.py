""" Serializers """

# Django Core imports
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

# Third party imports
from rest_framework import serializers

# App imports
from .models import Hero


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for users
    """

    class Meta:
        User = get_user_model()
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for groups
    """

    class Meta:
        model = Group
        fields = ["url", "name"]


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for heroes
    """

    class Meta:
        model = Hero
        fields = ["name", "alias"]
