#!/bin/bash

DOCKER_ID=`docker run -d -p 5000:5000 taschenrechner`
sleep 3

python3 test_app.py
EXIT_CODE=$?

docker stop $DOCKER_ID
docker rm $DOCKER_ID

exit $EXIT_CODE
