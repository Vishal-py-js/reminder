
## Setup

The first thing to do is to clone the repository:


git clone https://github.com/Vishal-py-js/reminder.git

cd reminder


Then install the dependencies:

pip install -r requirements.txt


Once `pip` has finished downloading the dependencies:

database setup:
run py manage.py makemigrations to prepare database tables
run py manage.py migrate to create database tables

run python manage.py runserver to start the server

And navigate to `http://127.0.0.1:8000/api/reminders/` to get all reminders created.

To add a new reminder make a POST request to `http://127.0.0.1:8000/api/create/`:
request body -  
{
    "message": "reminder message",
    "reminder_date":"2024-03-09T07:26:55.081193Z"
}
