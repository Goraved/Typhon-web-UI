#!/usr/bin/env bash

cd ..
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
deactivate