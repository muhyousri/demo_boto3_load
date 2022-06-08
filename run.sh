#!/bin/bash

while getopts 'cldh:' OPTION; do
  case "$OPTION" in
    c)
      python3 ./src/create.py
      ;;
    h)
      echo " usage: [-l] load [-c] create [-d] delete"
      ;;
    l)
      python3 ./src/load.py
      ;;
    d)
      python3 ./src/clean.py
      ;;
    ?)
      echo " usage: [-l] load [-c] create [-d] delete" >&2
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"