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
RUN_TESTS=
pip install -r requirements.txt --quiet

# Run The tests in project folder
py.test -n auto --dist=loadfile --tb=no ${dir}/tests/${RUN_TESTS} --alluredir ${dir}/allure_reports/archive/${_now}

## Environments settings
cp ${dir}/allure_reports/environment.properties ${dir}/allure_reports/archive/${_now}

## Copy previous history
mkdir ${dir}/allure_reports/archive/${_now}/history
cp ${dir}/allure_reports/history/*.json ${dir}/allure_reports/archive/${_now}/history

## Generate allure report folder
allure generate ${dir}/allure_reports/archive/${_now} -o ${dir}/allure_reports/archive/${_now}/generated-report

## Saving current test run to history
rm ${dir}/allure_reports/history/*
cp -r ${dir}/allure_reports/archive/${_now}/generated-report/history/*.json ${dir}/allure_reports/history

## Run server with generated allure report
#allure serve ${dir}/allure_reports/archive/${_now}

## Open generated report
allure open ${dir}/allure_reports/archive/${_now}/generated-report

# Send email with latest run
#python ${dir}/framework/send_email.py