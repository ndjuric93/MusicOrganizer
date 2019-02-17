FROM python:3.7.1-alpine3.8
LABEL maintainer="nemanja.djuric@outlook.com"

# Install Open RC (including rc-service)

RUN apk add openrc --no-cache

# Install GCC

RUN apk add build-base

# Install postgres libs

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

# Update apk and install librdkafka

RUN sed -i -e 's/v[[:digit:]]\.[[:digit:]]/edge/g' /etc/apk/repositories \
    && apk upgrade --update-cache --available                            \
    && apk --no-cache add librdkafka                                     \
    && apk --no-cache add librdkafka-dev

# Install MicroUtils

COPY dist/MicroUtilities-0.0.1.tar.gz .
RUN pip install MicroUtilities-0.0.1.tar.gz

# Install base requirements

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR '/'

ENV PYTHONPATH '/'
