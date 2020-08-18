FROM python:3.7.7-slim-buster

COPY . /cart_log_analyzer
WORKDIR /cart_log_analyzer

RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

ENV SECRET_KEY ""
ENV DEBUG ""
ENV PORT ""

ENTRYPOINT python manage.py migrate && \
           gunicorn --bind 0.0.0.0:$PORT cart_log_analyzer.wsgi
