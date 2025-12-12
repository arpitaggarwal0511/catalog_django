#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Optional: create a superuser non-interactively if env vars are provided
if [ -n "$DJANGO_SU_USERNAME" ] && [ -n "$DJANGO_SU_PASSWORD" ]; then
  echo "Ensuring superuser exists..."
  python - <<'PY'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
u = os.environ.get('DJANGO_SU_USERNAME')
p = os.environ.get('DJANGO_SU_PASSWORD')
e = os.environ.get('DJANGO_SU_EMAIL', '')
if u and not User.objects.filter(username=u).exists():
    User.objects.create_superuser(u, e or '', p)
    print("Superuser created:", u)
else:
    print("Superuser already exists or no username provided.")
PY
else
  echo "Superuser creation skipped (no DJANGO_SU_USERNAME/DJANGO_SU_PASSWORD)."
fi

echo "Starting Gunicorn..."
exec gunicorn catalog_back.wsgi:application --bind 0.0.0.0:10000 --workers 2
