#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Run Celery"

export C_FORCE_ROOT=1

echo "Compile Messages"
python manage.py compilemessages
# celery worker -A onlineBenevolent --concurrency=2 -E -B -l info
# command: celery worker --app=onlineBenevolent  --loglevel=info
exec celery worker -A onlineBenevolent --concurrency=2 -E -B -l info
