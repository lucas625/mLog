FROM python:3.8.6-slim-buster

COPY . /search_service
WORKDIR /search_service

RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

ENV SECRET_KEY ""
ENV DEBUG "true"
ENV SEARCH_SERVICE_PORT ""
ENV ELASTIC_SEARCH_URL ""
ENV ELASTIC_AUTH_USERNAME "elastic"
ENV ELASTIC_AUTH_PASSWORD "changeme"

ENTRYPOINT python manage.py migrate && \
           python manage.py runserver 0.0.0.0:$SEARCH_SERVICE_PORT
