""" Serializers """

# Django Core imports

# Third party imports
from rest_framework import serializers

# App imports
from .models import Appointment, Physician, Clinic, Patient, Pet


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for appointments
    """

    class Meta:
        model = Appointment
        fields = "__all__"


class PhysicianSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for physicians
    """

    class Meta:
        model = Physician
        fields = "__all__"


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for clinics
    """

    class Meta:
        model = Clinic
        fields = "__all__"


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for patients
    """

    class Meta:
        model = Patient
        fields = "__all__"


class PetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for pets
    """

    class Meta:
        model = Pet
        fields = "__all__"
