#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

if [ -n "$DJANGO_SU_USERNAME" ] && [ -n "$DJANGO_SU_PASSWORD" ]; then
  echo "Ensuring superuser exists..."
  python manage.py shell -c "from django.contrib.auth import get_user_model; \
u='${DJANGO_SU_USERNAME}'; p='${DJANGO_SU_PASSWORD}'; e='${DJANGO_SU_EMAIL:-}'; \
User=get_user_model(); \
if not User.objects.filter(username=u).exists(): \
    User.objects.create_superuser(u, e, p); \
    print('Superuser created:', u); \
else: \
    print('Superuser already exists:', u)"
else
  echo "Superuser creation skipped (no DJANGO_SU_USERNAME/DJANGO_SU_PASSWORD)."
fi

echo "Starting Gunicorn..."
exec gunicorn catalog_back.wsgi:application --bind 0.0.0.0:10000 --workers 2
