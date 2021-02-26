#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${SCRIPT_DIR}"

source .venv/bin/activate
python server.py
deactivate