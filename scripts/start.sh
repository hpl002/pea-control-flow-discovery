#!/bin/sh
# Will only run from basedir context
SERVER="$(realpath src/main.py)"
export FLASK_APP=$SERVER
flask run -p 80