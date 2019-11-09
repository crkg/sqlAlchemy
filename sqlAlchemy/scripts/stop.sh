#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
USER=`whoami`
PID_FILE="/Users/${USER}/PycharmProjects/gunicorn/var/run/server.pid"

#< add python installation if required ; and export path with python >

cd ${DIR}/..

if [ ! -f ${PID_FILE} ]; then
    echo "The file ${PID_FILE} does not exist, it seems server is already stopped"
    exit 0
fi

PID=`cat ${PID_FILE}`

kill -15 ${PID}

sleep 2

kill -0 ${PID}

if [ $? -eq 0 ]; then
    echo "Could not shut down server in time better investigate"
    exit 1
fi

rm -f ${PID_FILE}
