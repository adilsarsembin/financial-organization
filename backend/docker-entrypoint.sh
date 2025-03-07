#!/bin/sh

container_type=${CONTAINER_TYPE-DJANGO};

if [ "$container_type" = "DJANGO" ]; then
  python manage.py migrate --noinput
  python manage.py collectstatic --noinput
  gunicorn financial_organization.wsgi:application --bind 0.0.0.0:$PORT
fi;
