#!/usr/bin/env bash

set -e

exec python manage.py migrate --noinput

echo "Run django"
exec python manage.py runserver 0.0.0.0:8001
