#!/usr/bin/env bash
docker build -t typhon_web_image .
docker run --name test_container_web -i typhon_web_image
docker cp test_container_web:/Typhon/allure-results  ./
docker stop test_container_web
docker rm test_container_web


## Install allure
## Linux
#sudo apt-add-repository ppa:qameta/allure
#sudo apt-get update
#sudo apt-get install allure
## Mac
#brew install allure

## Open generated report
LATEST=$(ls -td allure-results/archive/*/ | head -1)
allure open $LATEST/generated-report