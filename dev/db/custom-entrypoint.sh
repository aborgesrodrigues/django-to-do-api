#!/bin/sh
dockerize -wait tcp://db:5432 -timeout 60s

echo "running migrations"
python3 manage.py migrate --skip-checks

echo "starting $@"
exec "$@"