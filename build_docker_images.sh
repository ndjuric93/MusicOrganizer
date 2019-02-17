#! /bin/bash

function build_service()
{
    cd "${1}"

    python setup.py sdist

    docker build -t micromusic-"${1}" .

    cd -
}


# Build utilities package

cd ${MICROUTILS_DIR}
python setup.py sdist

# Build base docker image

if [[ ! -z ${BASE_BUILD} ]]
then
    docker build -t base_services .
fi

cd ${MICROMUSIC_ROOT}/server

# Build services

build_service "gateway"
build_service "records"
build_service "users"
build_service "player"
build_service "statistics"
build_service "track_statistic_aggregation"
