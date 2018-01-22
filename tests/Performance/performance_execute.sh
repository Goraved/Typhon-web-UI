#!/usr/bin/env bash
# Open UI server
open http://127.0.0.1:8089/
locust -f locust_test.py

## run without UI c = count of users; r = hatch rate;
#locust -f --no-web -c 1000 -r 100 --run-time 1h30m