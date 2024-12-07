#!/bin/bash
WORK_DIR="$(dirname "$0")/.."

source "$WORK_DIR/.venv/bin/activate"
python3.12 "$WORK_DIR/autoRSA.py" "$@"