#!/bin/bash
source venv/bin/activate

_now=$(date +%Y-%m-%d_%H:%M:%S)
dir=$(pwd)


# Path to base folder of tests
PYTHONPATH="${PYTHONPATH}:${dir}"
export PYTHONPATH

## Set environment
env=$1
run_tests=$2
sed -i '' "1,/\(ENVIRONEMENT = \).*/ s/\(ENVIRONEMENT = \).*/ENVIRONEMENT = '${env}'/"  ${dir}/configuration/config_parse.py

# Run The tests in project folder
py.test -n auto --dist=loadfile --tb=no ${dir}/tests/${run_tests} --alluredir ${dir}/allureReports/archive/${_now}

## Environments settings
cp ${dir}/allureReports/environment.properties ${dir}/allureReports/archive/${_now}

## Copy previous history
mkdir ${dir}/allureReports/archive/${_now}/history
cp ${dir}/allureReports/history/*.json ${dir}/allureReports/archive/${_now}/history

## Generate allure report folder
allure generate ${dir}/allureReports/archive/${_now} -o ${dir}/allureReports/archive/${_now}/generated-report

## Saving current test run to history
rm /Users/Grave/PycharmProjects/automated-tests/allureReports/history/*
cp -r ${dir}/allureReports/archive/${_now}/generated-report/history/*.json ${dir}/allureReports/history

## Run server with generated allure report
##allure serve ${dir}/allureReports/archive/${_now}

## Open generated report
allure open ${dir}/allureReports/archive/${_now}/generated-report

# Send email with latest run
#python ${dir}/framework/send_email.py