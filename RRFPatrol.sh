#!/bin/sh

PATH_SCRIPT='/opt/RRFPatrol/RRFPatrol.py'
PATH_PID='/tmp'

case "$1" in
    start)
        echo "Starting RRFPatrol"
        nohup python3 $PATH_SCRIPT > /dev/null 2>&1 & echo $! > $PATH_PID/RRFPatrol.pid
        ;;
    stop)
        echo "Stopping RRFPatrol"
        kill `cat $PATH_PID/RRFPatrol.pid`
        ;;
    esac%