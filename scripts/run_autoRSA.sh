#!/bin/bash
WORK_DIR="$(dirname "$0")/.."

source "$WORK_DIR/.venv/bin/activate"
python "$WORK_DIR/autoRSA.py" 'buy' '1' 'AAPL' 'all' 'false'