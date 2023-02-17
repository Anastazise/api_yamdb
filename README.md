# YaMDb

# Description

YaMDb is online database for reviews to titles such as films, books and music.

Each user can post a review for any title with raiting 1 to 10, and leave a comment to any review.

Build with Django Rest Framework.

Authorisation implemented with JWT tokens.

Documented auto-generated by Redoc.

# Intallation:

## - Clone ripository

## - Create, and activate vertual enviroment

python -m venv venv

source venv/scripts/activate

## - Install requirements
python -m pip install --upgrade pip
python pip install -r requirements.txt

## - Make migrations
python manage.py makemigrations
python manage.py migrate

## - Run server
python manage.py runserver

# API docs could be found here:
http://127.0.0.1:8000/redoc/
