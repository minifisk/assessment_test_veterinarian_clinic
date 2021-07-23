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
        fields = ["physician", "date", "timeslot", "patient", "notes"]


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
        fields = ["name", "website", "city", "phone_number"]


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for patients
    """

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "email", "phone_number"]


class PetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for pets
    """

    class Meta:
        model = Pet
        fields = ["name", "animal_type", "email", "phone_number"]
