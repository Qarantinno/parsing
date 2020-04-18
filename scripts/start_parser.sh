#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

cd "${SCRIPT_PATH}/.."
if [ -d /app/docker_env/docker_deps_installed ]; then
  source ./dev/bin/activate
  python -m api.main && echo "Parsing done well"
else
  echo "Dependencies are not installed yet!"
fi;