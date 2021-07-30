""" Models """

from django.db import models

# Create your models here.

TIMESLOT_LIST = (
    (0, "09:00 - 09:30"),
    (1, "09:30 - 10:00"),
    (2, "10:00 - 10:30"),
    (3, "10:30 - 11:00"),
    (4, "11:00 - 11:30"),
    (5, "11:30 - 12:00"),
    (6, "12:00 - 12:30"),
    (7, "12:30 - 13:00"),
    (8, "13:00 - 13:30"),
    (9, "13:30 - 14:00"),
    (10, "14:00 - 14:30"),
    (11, "14:30 - 15:00"),
    (12, "15:00 - 15:30"),
    (13, "15:30 - 16:00"),
    (14, "16:00 - 16:30"),
    (15, "16:30 - 17:00"),
)

class Appointment(models.Model):
    """
    DB model for appointments
    """

    class Meta:
        unique_together = ("physician", "date", "timeslot")

    physician = models.ForeignKey("Physician", on_delete=models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD", null=False)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, null=False)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    notes = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return "{} {} {}. Patient: {}".format(self.date, self.time, self.physician, self.patient)

    @property
    def time(self):
        """Extracting the string from the list"""
        return TIMESLOT_LIST[self.timeslot][1]


class Physician(models.Model):
    """
    DB model for physicians
    """

    SPECIALITY_LIST = (("SM", "Small pets"), ("LG", "Large pets"), ("AN", "Antesthesia"))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    speciality = models.CharField(choices=SPECIALITY_LIST, max_length=2)
    clinic = models.ForeignKey("Clinic", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}. Speciality: {}".format(
            self.first_name, self.last_name, self.clinic, self.speciality
        )


class Clinic(models.Model):
    """
    DB model for Clinics
    """

    name = models.CharField(max_length=50, null=False)
    website = models.URLField(max_length=150, null=False)
    city = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "{} {}".format(self.name, self.city)


class Patient(models.Model):
    """
    DB model for Patients (humans owning pets)
    """

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    pets = models.ForeignKey("Pet", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Pet(models.Model):
    """
    DB model for Pets (owned by patient)
    """

    ANIMAL_LIST = (("DG", "Dog"), ("CT", "Cat"), ("HR", "Horse"))

    name = models.CharField(max_length=30, null=False)
    animal_type = models.CharField(choices=ANIMAL_LIST, max_length=2, null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return "{} {}".format(self.name, self.animal_type)
