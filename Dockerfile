FROM python:3

env PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE fampay.settings

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN python manage.py migrate

COPY . /app