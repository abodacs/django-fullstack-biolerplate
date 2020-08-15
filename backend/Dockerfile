FROM python:3.8

RUN locale-gen C.UTF-8 || true
# set environment variables
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8
ENV DEBIAN_FRONTEND noninteractive
ARG ENVIRONMENT=development


RUN groupadd appuser && useradd --home /home/appuser -g appuser appuser
RUN mkdir -p /home/appuser/app/backend
WORKDIR /home/appuser/app/backend

# Install system dependencies
RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    apt-get install python-dev  python-pip -y && \
    apt-get install python3-dev python3-pip python3-venv python3-wheel -y && \
    python3 -m pip install wheel

# set timezone to UTC
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime


# REQUIREMENTS
COPY backend/requirements/ /requirements/

# install python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --user --default-timeout=100 -r /requirements/${ENVIRONMENT}.txt

# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm -fr /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

# ADD backend/ /home/appuser/app/backend

COPY backend/start.sh /usr/local/bin/
COPY backend/entrypoint.sh /usr/local/bin/


RUN chmod +x /usr/local/bin/start.sh && \
    chmod +x /usr/local/bin/entrypoint.sh

USER appuser

EXPOSE 8001
STOPSIGNAL SIGTERM

# ENV PYTHONPATH=/home/appuser/app/backend


CMD /usr/local/bin/start.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]