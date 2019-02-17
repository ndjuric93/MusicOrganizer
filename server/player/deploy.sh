#!/usr/bin/env bash

export SERVICE_DIR=${MICROMUSIC_ROOT}/server/player

if [[ "${BUILD}" == 1 ]]
then
    echo ${SERVICE_DIR}
    python ${SERVICE_DIR}/setup.py sdist
    cd ${MICROUTILS_DIR}
    python ${MICROUTILS_DIR}/setup.py sdist
    cp ${MICROUTILS_DIR}/dist/* ${SERVICE_DIR}/dist/
    cd -
    docker build -t micromusic-player .
fi

docker run -ti -v ~/Workspaces/scratch:/scratch             \
    -e SERVER_ADDRESS=0.0.0.0                               \
    -e SERVER_PORT=5000                                     \
    -e KAFKA_ADDRESS=${KAFKA_ADDRESS}                       \
    -e KAFKA_PORT=9092                                      \
    --network micromusic                                    \
    -p 5001:5000                                            \
    --name player                                           \
    micromusic-player
