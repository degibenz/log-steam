FROM python:3.7-slim

LABEL maintainer='Aleksey Shkil <alecseishkill@gmail.com>'

RUN apt-get -y update \
    && apt-get -y install apt-utils build-essential git libpq5 libpq-dev \
    && apt-get clean

COPY config /app/config

COPY Makefile /app/Makefile

COPY Pipfile Pipfile.lock /app/

COPY src /app/src/

WORKDIR /app

RUN make pyenv