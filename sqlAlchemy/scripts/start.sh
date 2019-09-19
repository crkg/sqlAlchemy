#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
USER=`whoami`
PID_FILE="/Users/${USER}/PycharmProjects/gunicorn/var/run/server.pid"

#< add python installation if required ; and export path with python >

cd ${DIR}/..

export CONFFILE_PATH=../config/app_conf_local.py


# pip3 install -r requirements.txt

echo "checking db upgrade"

#python3 manage.py db upgrade 2>&1

echo "Starting gunicorn"

gunicorn manage:app -c config/gunicorn_conf.py --pid ${PID_FILE}

echo "started the service"
