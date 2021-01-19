### Build and install packages
FROM python:3.8 as build-python

ARG ENVIRONMENT=development

RUN apt-get -y update \
  && apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


# REQUIREMENTS
COPY backend/requirements/ /requirements/

# install python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --default-timeout=100 -r /requirements/${ENVIRONMENT}.txt

### Final image
FROM python:3.8-slim

# create the app user
RUN groupadd --gid 1000 appuser && useradd -u 1000 -g appuser appuser

# set timezone to UTC
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime


RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y gcc build-essential \
  && apt-get install -y python3-pip python3-wheel \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Install system dependencies
  && python3 -m pip install wheel

# chown all the files to the app user
RUN chown -R appuser:appuser $HOME

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $HOME
RUN mkdir -p $APP_HOME

COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/

# copy project
COPY . $APP_HOME

# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    # cleaning up unused files
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -fr /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*

COPY backend/start.sh /usr/local/bin/
COPY backend/start_celery.sh /usr/local/bin/
COPY backend/entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/start.sh && \
    chmod +x /usr/local/bin/start_celery.sh&& \
    chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8001
STOPSIGNAL SIGTERM

# set environment variables
ENV LANG C.UTF-8
ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

WORKDIR "${APP_HOME}/backend"

ENV PYTHONPATH "${PYTHONPATH}:${HOME}/.local/bin"

CMD /usr/local/bin/start.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
