#!/bin/sh
SERVER="$(realpath ../src/main.py)"
export FLASK_APP=$SERVER
flask run -p 8080