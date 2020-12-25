#!/bin/sh
# Will only run from basedir context
SERVER="$(realpath src/main.py)"
export FLASK_APP=$SERVER
export FLASK_ENV=development
flask run -p 8080