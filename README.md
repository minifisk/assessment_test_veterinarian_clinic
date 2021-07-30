# Booking system for veterenarian clinic
This is an assessment test I did in July 2021 for a position as a back-end engineer, I originally had 5 hours to create the project and have complemented the program with around 3-4 more hours of work.
The program provide three endpoints aimed to be used by the front-end engineers to:
1) See which timeslots on a specific date that a certain Physician have booked with clients
2) See all past and future timeslots booked, grouped by date, for a certain Physician
3) Create new appointments

## Installment instructions
1) Clone project to your local machine
2) Install pipenv dependencies with "pipenv install" (install pipenv with pip3 install pipenv if you don't have it installed globally)
3) Run pipenv shell to initialize virtual environment
4) Run migrations with "python manage.py makemigrations" and "python manage.py migrate"
5) Run server with "python manage.py runserver"

## Usage instructions
1) Create a superuser with "python manage.py createsuperuser" and go to localhost/admin and log in to add a new appointment and try out the program.
2) Go to localhost/first_name_of_your_physcian/last_name_of_your_physician/date_of_appointment (fill in the variables with data from the appointment your created in step 1)
3) You should now see the appointment for this date, you can create more appointments on this date and they should show up here
4) Go to localhost/first_name_of_your_physcian/last_name_of_your_physician/ to see all appointments grouped by date
5) Go to localhost/bookings to create additional bookings (can only use the physicians & patients that you have created in the admin interface)

## Testing
If you want to run tests on the program run "python manage.py tests" - you can find the unit tests in myproject/rest_api/tests.py if you want to inspect what is being tested
