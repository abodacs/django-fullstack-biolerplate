#!/usr/bin/env bash

set -e

echo "Run django"
exec python manage.py runserver 0.0.0.0:8001
