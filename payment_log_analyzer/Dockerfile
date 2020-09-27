FROM python:3.7.7-slim-buster

COPY . /payment_log_analyzer
WORKDIR /payment_log_analyzer

RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

ENV SECRET_KEY ""
ENV PAYMENT_LOG_ANALYZER_PORT ""

ENTRYPOINT python manage.py migrate && \
           python manage.py runserver 0.0.0.0:$PAYMENT_LOG_ANALYZER_PORT
