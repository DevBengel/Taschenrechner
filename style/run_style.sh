#!/bin/bash

docker build -t test_style:v1 .
DOCKER_ID=`docker run -d test_style:v1`
sleep 5

docker cp ../main.py $DOCKER_ID:/code

docker exec $DOCKER_ID pylint --exit-zero --output-format=text main.py | tee pylint.txt
docker exec $DOCKER_ID pylint --exit-zero --output-format=pylint_gitlab.GitlabCodeClimateReporter main.py > codeclimate.json
docker exec $DOCKER_ID pylint --exit-zero --output-format=pylint_gitlab.GitlabPagesHtmlReporter main.py > pylint.html
EXIT_CODE=$?

docker stop $DOCKER_ID
docker rm $DOCKER_ID
docker rmi test_style:v1
exit $EXIT_CODE
