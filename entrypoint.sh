#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:8000 --workers 3 core.wsgi:application
