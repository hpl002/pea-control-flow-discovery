#!/bin/sh
# Will only run from basedir context
SERVER="$(realpath src/main.py)"
echo $SERVER
export FLASK_APP=$SERVER
flask run -p 8080