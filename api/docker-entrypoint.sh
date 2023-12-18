#!/bin/sh

set -e

# activate our virtual environment
. /opt/pysetup/.venv/bin/activate

# Evaluating passed command
exec "$@"
