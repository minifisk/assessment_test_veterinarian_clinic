""" TESTS """

# Core django imports
from django.test import TestCase

# App imports
from .models import Appointment, Physician, Clinic, Patient, Pet

# Create your tests here.

class AppointmentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a clinic
        cls.clinic = Clinic.objects.create(name="Testclinic", website="www.testclinic.com", city="Stockholm", phone_number="08-604 10 66")
        
        # Create a physician
        cls.physician = Physician.objects.create(first_name="John", last_name="Doe", email="John@Doe.com", speciality="SM", clinic=cls.clinic)

        # Create a pet
        cls.pet = Pet.objects.create(name="Doggo", animal_type="DG", age=5)

        # Create a patient
        cls.patient = Patient.objects.create(first_name="Patient firstname", last_name="Patient Lastname", email="patient@meail.com", phone_number="08-604 42 62", pets=cls.pet)

        # Create an appointment
        cls.appointment = Appointment.objects.create(physician=cls.physician, date="2021-07-30", timeslot=0, patient=cls.patient)

    def test_appointment_date_view(self):
        response = self.client.get("/bookings/{}/{}/{}".format(self.physician.first_name, self.physician.last_name, self.appointment.date))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, ["09:00 - 09:30"])

    def test_physician_booking_view(self):
        response = self.client.get("/bookings/{}/{}/".format(self.physician.first_name, self.physician.last_name))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"2021-07-30": ["09:00 - 09:30"]})

    def test_create_new_appointment(self):
        response = self.client.post("/bookings/", {"phyisician": "1", "patient": "1", "timeslot": "0", "date": "2021-07-30"})
        self.assertEqual(response.status_code, 200)
        print(response)

