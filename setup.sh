#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${SCRIPT_DIR}"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt