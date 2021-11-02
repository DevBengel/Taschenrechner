#!/bin/bash

docker network inspect testlbtaschenrechner

if [[ $? -ne 0 ]]; then
    docker network create --subnet=172.20.20.0/24 --gateway=172.20.20.1 testlbtaschenrechner
fi

DOCKER_LB_ID=`docker run --net testlbtaschenrechner --ip 172.20.20.10 -p 3333:3333 -itd 10.20.1.82:1234/root/application/lb`
DOCKER_APP1_ID=`docker run --net testlbtaschenrechner --ip 172.20.20.101 -itd 10.20.1.82:1234/root/application/app`
DOCKER_APP2_ID=`docker run --net testlbtaschenrechner --ip 172.20.20.102 -itd 10.20.1.82:1234/root/application/app`
sleep 5

python3 test_system.py
EXIT_CODE=$?

docker stop $DOCKER_LB_ID
docker rm $DOCKER_LB_ID
docker stop $DOCKER_APP1_ID
docker rm $DOCKER_APP1_ID
docker stop $DOCKER_APP2_ID
docker rm $DOCKER_APP2_ID
docker network rm testlbtaschenrechner
exit $EXIT_CODE

