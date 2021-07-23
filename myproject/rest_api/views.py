# pylint: disable=too-many-ancestors
""" Views """

# Django core imports

# Third party imports
from rest_framework import permissions, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import bleach


# App imports
from .serializers import (
    AppointmentSerializer,
    PhysicianSerializer,
    ClinicSerializer,
    PatientSerializer,
    PetSerializer,
)
from .models import Appointment, Physician, Clinic, Patient, Pet


def strip_xss(text):
    """Remove all markup from text."""

    allowed_tags = []
    allowed_attributes = []
    allowed_styles = []

    text = bleach.clean(
        text, allowed_tags, allowed_attributes, allowed_styles, strip=True, strip_comments=True
    ).strip()

    return text


class AppointmentViewset(viewsets.ModelViewSet):
    """
    API viewset endpoint for viewing and editing appointments
    """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentView(APIView):
    """
    API view for appointments
    """

    permission_classes = []

    def get(self, request, physician_first_name, physician_last_name, date):
        """
        Return available time-slots for requested physician and date
        """

        unsafe_physician_first_name = physician_first_name
        unsafe_physician_last_name = physician_last_name
        unsafe_date = date

        sanitized_physician_first_name = strip_xss(unsafe_physician_first_name)
        sanitized_physician_last_name = strip_xss(unsafe_physician_last_name)
        sanitized_date = strip_xss(unsafe_date)

        sanitized_physician_context = {
            "first_name": sanitized_physician_first_name,
            "last_name": sanitized_physician_last_name,
        }

        physician_serializer = PhysicianSerializer(data=sanitized_physician_context)

        """ SHOULD HERE VALIDATE PHYSICIAN, WAS NOT ABLE TO DO IT DUE TO
        THAT SERIALIZER HAD TO RECEIVE ALL FIELDS  """

        ### PERFORM LOGIC

        physician = Physician.objects.filter(first_name=sanitized_physician_first_name).filter(
            last_name=sanitized_physician_last_name
        )

        appointments_this_date = Appointment.objects.filter(physician=physician[0])

        print(appointments_this_date[0].time)

        return Response("Hello")
