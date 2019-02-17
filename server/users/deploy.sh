#!/usr/bin/env bash

export SERVICE_DIR=${MICROMUSIC_ROOT}/server/player

#if [[ "${BUILD}" == 1 ]]
#then
python setup.py sdist
docker build -t micromusic-users .
#fi

#docker run -ti -v ~/Workspaces/scratch:/scratch             \
#    -e SERVER_ADDRESS=0.0.0.0                               \
#    -e SERVER_PORT=5000                                     \
#    -e KAFKA_ADDRESS=${KAFKA_ADDRESS}                       \
#    -e KAFKA_PORT=9092                                      \
#    --network micromusic                                    \
#    -p 5001:5000                                            \
#    --name player                                           \
#    micromusic-player
