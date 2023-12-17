#!/bin/sh

set -e

# activate our virtual environment
. /opt/pysetup/.venv/bin/activate

# run migrations
alembic upgrade head

# Evaluating passed command
exec "$@"
