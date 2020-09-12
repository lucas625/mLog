FROM python:3.7.7-slim-buster

COPY . /csv_service
WORKDIR /csv_service

RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

ENV SECRET_KEY ""
ENV DEBUG ""
ENV CSV_SERVICE_PORT ""

ENTRYPOINT python manage.py migrate && \
           gunicorn --bind 0.0.0.0:$CSV_SERVICE_PORT csv_service.wsgi
