from django.contrib import admin
from .models import Appointment, Physician, Clinic, Patient, Pet

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Physician)
admin.site.register(Clinic)
admin.site.register(Patient)
admin.site.register(Pet)
