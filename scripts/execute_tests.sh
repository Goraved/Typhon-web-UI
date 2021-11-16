#!/bin/bash
if [[ ! -f requirements.txt ]]; then
    cd ..
fi
source venv/bin/activate

_now=$(date +%Y-%m-%d_%H:%M:%S)
dir=$(pwd)


# Path to base folder of tests
PYTHONPATH="${PYTHONPATH}:${dir}"
export PYTHONPATH

## Set environment
ENVIRONMENT=DEV
RUN_TESTS=ui
pip install -r requirements.txt --quiet
mkdir -p allure-results
mkdir -p allure-results/archive
mkdir -p allure-results/history

# Run The tests in project folder
py.test -n auto --dist=loadfile --tb=no ${dir}/tests/${RUN_TESTS} --alluredir ${dir}/allure-results/archive/${_now}

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

## Run server with generated allure report
#allure serve ${dir}/allure-results/archive/${_now}

## Open generated report
allure open ${dir}/allure-results/archive/${_now}/generated-report

# Send email with latest run
#python ${dir}/framework/send_email.py