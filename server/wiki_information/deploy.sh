#!/usr/bin/env bash

export SERVICE_DIR=${MICROMUSIC_ROOT}/server/wiki_information

python setup.py sdist
docker build -t micromusic-wiki_information .