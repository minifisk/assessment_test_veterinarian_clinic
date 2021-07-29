""" FORMS """

from django import forms
import datetime

from .models import Physician, Patient, TIMESLOT_LIST

class BookingForm(forms.Form):
    physician = forms.ModelChoiceField(queryset=Physician.objects.all())
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    timeslot = forms.ChoiceField(choices=TIMESLOT_LIST)
    date = forms.DateField(initial=datetime.date.today)
    notes = forms.CharField(max_length=1500, required=False)