#!/bin/bash

if [ ! "$(docker network ls | grep micromusic)" ]; then
  echo "Creating micromusic network ..."
  docker network create --subnet=172.18.0.0/16 micromusic
else
  echo "micromusic network exists."
fi


echo "Starting zookeeper"

docker run                                                                       \
           -p 2181:2181                                                          \
           --name zookeeper                                                      \
           --network micromusic                                                  \
           blacktop/kafka zookeeper-server-start.sh config/zookeeper.properties

echo "Starting kafka node"

docker run -d                                             \
           -v /var/run/docker.sock:/var/run/docker.sock   \
           -e KAFKA_ADVERTISED_HOST_NAME=${KAFKA_ADDRESS} \
           --network micromusic                           \
           -p 9092:9092                                   \
           --name micromusic                              \
           blacktop/kafka
