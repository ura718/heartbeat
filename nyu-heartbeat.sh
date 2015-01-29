#!/bin/sh

# Source function library.
. /etc/rc.d/init.d/functions


prog="nyu-heartbeat"
lockfile="/var/lock/subsys/$prog"

start() {

    echo -n $"Starting nyu-heartbeat: "
    /home/ym26/scripts/heartbeat/server.py &
    retval=$?
    if [[ $retval == 0 ]]; then
	touch $lockfile
	success
    else
	failure
    fi
    echo
    return $retval
}

stop() {
    echo -n $"Stopping nyu-heartbeat: "
    killall server.py
    retval=$?
    if [[ $retval == 0 ]]; then
	rm -f $lockfile
	success
    else
	failure
    fi
    echo
    return $retval
}





# See how we were called.
case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  status)
        status $prog
	RETVAL=$?
	;;
  restart)
	stop
	start
	;;
  *)
	echo $"Usage: $prog {start|stop|restart|status}"
	RETVAL=2
esac

exit $RETVAL
