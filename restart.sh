#!/bin/bash

$(dirname "${BASH_SOURCE[0]}")/build_docker_images.sh

docker-compose -f $(dirname "${BASH_SOURCE[0]}")/server/docker-compose.yml up

