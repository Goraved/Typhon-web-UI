#!/usr/bin/env bash
dir=$(pwd)


# Path to base folder of tests
PYTHONPATH="${PYTHONPATH}:${dir}"
export PYTHONPATH

virtualenv -p /usr/bin/python3 venv || venv -p /usr/bin/python virtualenv
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
sh install_requirements.sh
