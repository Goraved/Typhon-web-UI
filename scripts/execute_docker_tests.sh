#!/bin/bash
if [[ ! -f requirements.txt ]]; then
    cd ..
fi
. /opt/venv/bin/activate

_now=$(date +%Y-%m-%d_%H:%M:%S)
dir=$(pwd)

## Set environment
ENVIRONMENT=DEV
DOCKER_RUN=True
export DOCKER_RUN
RUN_TESTS=${RUN_TESTS:=ui}

mkdir -p allure-results
mkdir -p allure-results/archive
mkdir -p allure-results/history

# Run The tests in project folder
echo "Running tests"
# Regular run
python -m pytest -n auto --dist=loadfile tests/${RUN_TESTS} --alluredir ${dir}/allure-results/archive/${_now}
echo "Test run finished"

## Environments settings
cp ${dir}/allure-results/environment.properties ${dir}/allure-results/archive/${_now}

## Copy previous history
mkdir ${dir}/allure-results/archive/${_now}/history
cp ${dir}/allure-results/history/*.json ${dir}/allure-results/archive/${_now}/history

## Generate allure report folder
allure generate ${dir}/allure-results/archive/${_now} -o ${dir}/allure-results/archive/${_now}/generated-report

## Saving current test run to history
rm ${dir}/allure-results/history/*
cp -r ${dir}/allure-results/archive/${_now}/generated-report/history/*.json ${dir}/allure-results/history
find . | grep -E "(__pycache__|\.pyc|\.pyo$|.pytest_cache)" | xargs rm -rf