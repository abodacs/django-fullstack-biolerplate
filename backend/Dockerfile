FROM python:3.8

RUN locale-gen C.UTF-8 || true
RUN DEBIAN_FRONTEND noninteractive
# set environment variables
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8
ARG ENVIRONMENT=development


RUN groupadd user && useradd  -disabled-password  --gecos "" --home /home/appuser -g appuser appuser
WORKDIR /home/appuser/app/backend

# Install system dependencies
RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    python3 -m pip install --no-cache-dir pip-tools

# set timezone to UTC
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime


# REQUIREMENTS
COPY backend/requirements/ /requirements/

# install python dependencies
RUN python3 -m pip install -r /requirements/${ENVIRONMENT}.txt

# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

ADD backend/ /home/appuser/app/backend

USER appuser

EXPOSE 8001
STOPSIGNAL SIGTERM

CMD uvicorn djangoFullstack.asgi:application --port 8001--reload
