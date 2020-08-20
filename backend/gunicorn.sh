#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

#echo "Collect static"
#python manage.py collectstatic --noinput


echo "Compile Messages"
python manage.py compilemessages

echo "Run gunicorn"
exec gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker onlineBenevolent.asgi:application --worker-tmp-dir /dev/shm --timeout 120 \
    --max-requests=2000 \
    --max-requests-jitter=300 \
    --bind 0.0.0.0:8001
