FROM python:3.7.7-slim-buster

COPY . /search_service
WORKDIR /search_service

RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

ENV SECRET_KEY ""
ENV DEBUG ""
ENV SEARCH_SERVICE_PORT ""

ENTRYPOINT python manage.py migrate && \
           gunicorn --bind 0.0.0.0:$SEARCH_SERVICE_PORT search_service.wsgi
