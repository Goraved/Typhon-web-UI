#!/usr/bin/env bash
# Setup
dir=$(pwd)
PYTHONPATH="${PYTHONPATH}:${dir}"
export PYTHONPATH

# Open UI server
open http://127.0.0.1:8089/
locust -f load_tests/load_test_example.py

## run without UI c = count of users; r = hatch rate;
#results=test_results_$(date +%Y-%m-%d_%H:%M:%S)
#mkdir tests/Load/${results}
#cd tests/Load/${results}
#locust -f ../load_test_example.py --csv=foobar --no-web -c 100 -r 5 --run-time 1h30m
