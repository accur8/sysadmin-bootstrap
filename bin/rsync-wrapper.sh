#!/bin/sh
 
logger -t backup $@
/usr/bin/sudo /usr/bin/rsync "$@";