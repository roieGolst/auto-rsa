#!/bin/bash
WORK_DIR="$(dirname "$0")/.."

cd "$WORK_DIR" || echo "Failed moving to working dir"
source ./.venv/bin/activate
./.venv/bin/python3.12 ./autoRSA.py "$@"