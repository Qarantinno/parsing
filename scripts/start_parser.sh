#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

#Dot env
if [[ ! -f "${SCRIPT_PATH}/../docker_env/.env" ]]; then
    echo ".env file not found! Process was stopped";
    exit 1
else
  set -a
  . "${SCRIPT_PATH}/../docker_env/.env"
  set +a
fi;

cd "${SCRIPT_PATH}/.."
if [ -d /app/docker_env/docker_deps_installed ]; then
  source ./dev/bin/activate
  python -m api.main && echo "Parsing done well"
else
  echo "Dependencies are not installed yet!"
fi;