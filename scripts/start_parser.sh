#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

cd "${SCRIPT_PATH}/.."
source ./dev/bin/activate
python -m api.main && echo "Parsing done well"