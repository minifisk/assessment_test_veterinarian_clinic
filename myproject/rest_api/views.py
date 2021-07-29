# pylint: disable=too-many-ancestors
""" Views """

# Django core imports
from collections import defaultdict
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Third party imports
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# App imports
from .serializers import (PhysicianSerializer)
from .models import Appointment, Patient, Physician
from .forms import BookingForm


class AppointmentDateView(APIView):
    """
    API view to see what timeslots a specific physician has appointments
    on a specific date.
    """

    permission_classes = []

    def get(self, request, physician_first_name, physician_last_name, date):
        """
        GET: Return time-slots of appointments on a certain date for the requested physician
        """

        # Validate incoming data against Physician model
        context = {
            "first_name": physician_first_name,
            "last_name": physician_last_name,
        }


        physician_serializer = PhysicianSerializer(data=context)

        if physician_serializer.is_valid():

            # Get queried physician and his/hers appointments for this date
            try:
                physician = Physician.objects.filter(first_name=physician_first_name, last_name=physician_last_name)
                appointments_this_date = Appointment.objects.filter(physician=physician[0], date=date)
            # Return exception with indstructions
            except:
                raise serializers.ValidationError(
                    "Could not find inputed physician or date was input incorrectly, supply with www.hostname/firstname/lastname/date - example: 'http://127.0.0.1:8000/bookings/alexander/lindgren/2021-07-23'"
                )

        else:
            raise serializers.ValidationError(
                physician_serializer.errors
            )

        # Prepare appointments for this date for http response to endpoint 
        appointment_list = []

        for appointment in appointments_this_date:
            appointment_list.append(appointment.time)

        # Return bookings for this date
        return Response(appointment_list)


class PhysicianBookings(APIView):
    """
    GET: API View to get see all bookings (past and future) for a physician, grouped by date
    """

    permission_classes = []

    def get(self, request, physician_first_name, physician_last_name):
        """
        Return time-slots of appointments on a certain date for
        the requested physician
        """

        # Validate incoming data against Physician model
        context = {
            "first_name": physician_first_name,
            "last_name": physician_last_name,
        }

        physician_serializer = PhysicianSerializer(data=context)

        if physician_serializer.is_valid():

            # Get queried physician and his/hers appointments
            try:
                physician = Physician.objects.filter(first_name=physician_first_name, last_name=physician_last_name)
                appointments = Appointment.objects.filter(physician=physician[0])

            # Return exception with instructions
            except:
                raise serializers.ValidationError(
                    "Could not find inputed physician, supply with www.hostname/firstname/lastname - example: 'http://127.0.0.1:8000/bookings/alexander/lindgren/'"
                )

        else:
            raise serializers.ValidationError(
                physician_serializer.errors
            )

        # Prepare appointments for for http response to endpoint 
        appointment_dict = defaultdict(list)

        for appointment in appointments:
            appointment_dict[str(appointment.date)].append(appointment.time)

        # Return bookings for this date
        return Response(appointment_dict)


def Booking(request):
    """ 
    GET: Render form for submitting new bookings 
    POST: Handle submitting form and registrating new appointment to DB
    """
    # If form is submitted, validate form and create new appointment
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():

            physician = Physician.objects.get(pk=request.POST["physician"])
            patient = Patient.objects.get(pk=request.POST["patient"])
            timeslot = request.POST["timeslot"]
            date = request.POST["date"]
            try: 
                new_appointment = Appointment.objects.create(physician=physician, patient=patient, timeslot=timeslot, date=date)
            except Exception as e:
                print(e)

            # Return user to page with Physicians all bookings (including new one)
            return HttpResponseRedirect("{}/{}/".format(physician.first_name, physician.last_name))

    # If user request view, render template for creating new appointments
    if request.method == "GET":
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})