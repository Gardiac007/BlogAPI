#!/bin/bash

echo "Starting Django application setup..."

echo "Cleaning up database..."
rm -f /app/db.sqlite3

echo "Cleaning up migration files..."
find /app -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /app -path "*/migrations/*.pyc" -delete

echo "Creating migrations..."
python manage.py makemigrations Authentication || echo "Authenticaion migrations failed!!!"
python manage.py makemigrations blog_app || echo "blog_app migrations failed!!!"

echo "Applying migrations..."
python manage.py migrate

echo "Setup complete! Starting Django server..."
python manage.py runserver 0.0.0.0:8000