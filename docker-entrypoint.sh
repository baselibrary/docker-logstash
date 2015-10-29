#!/bin/bash

#enable job control in script
set -e -m

#####   variables  #####

# add command if needed
if [ "${1:0:1}" = '-' ]; then
  set -- logstash "$@"
fi

#run command in background
if [ "$1" = 'logstash' ]; then
  ##### pre scripts  #####
  echo "========================================================================"
  echo "initialize:"
  echo "========================================================================"
  
  ##### run scripts  #####
  echo "========================================================================"
  echo "startup:"
  echo "========================================================================"
  exec gosu logstash "$@" &

  ##### post scripts #####
  echo "========================================================================"
  echo "configure:"
  echo "========================================================================"
  
  #bring command to foreground
  fg
else
  exec "$@"
fi
