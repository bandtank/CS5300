# Introduction
This application allows a user to book a time to see one or more movies. It is a simple application that works with a single user, which is due to the way the requirements were worded. The features are as follows:
* View a list of movies with the associated ratings, run times, descriptions, and show times
* Select show times and seats, which are then confirmed as a unique booking
* View a list of confirmed bookings on a history page
* Interact with the seat, movie, and booking data through an API

This application is based on the Django 5.1.6 framework. The files are organized as follows:
* `homework2/` - This is the root of the project
* `movie_theater_booking/` - This is the main project folder with the `manage.py` script and various other Django-included utilities.
* `bookings/` - This is the location of the `Bookings` application, which is the only custom application in the project.
* `bookings/api/` - This is the location of the API endpoints. The API can be accessed via REST at `{urlBase}/api/`.
* `bookings/templates/` - This is the location of the HTML templates for the MVT architecture.
* `uploads/` - This is the location of `MEDIA_ROOT` in the Django project. All user uploads and public files will be stored here.
* All dates and times are localized for the user, while the application only stores dates and times in UTC.
* All other application files can be found in `bookings/`, and all other project files can be found in the root folder as well as `movie_theater_bookings/`.

# Configuration
This project is built for the DevEdu environment. To run the application, the source code must be cloned or copied to a DevEdu instance, an environment must be created, and the webserver must be started. The following instructions allow the application to run:
* Clone the repository or copy the source code to a DevEdu instance
* Change directory to the project's root folder. E.g., `cd ~/aandrian/homework02/movie_theater_booking`
* Check the version of Python. This application is built to use Python 3.12.3.
```
python3 --version
```
* Create a virtual environment:
```
python3 -m venv venv
```
* Active the virtual environment:
```
. venv/bin/activate
```
* Install the dependencies:
```
python -m pip install -r requirements.txt
```
* Run the application:
```
python manage.py runserver 0.0.0.0:3000
```
* Navigate to the public URL of the DevEdu instance, or click the `App` button on the container's management page.

# Testing
To run the tests for the application, run the following commands from the project's root folder:
### Run all tests
```
python manage.py test
```
### Test coverage
```
coverage run --source='.' manage.py test
```