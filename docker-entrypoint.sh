#!/bin/ash

pip install --no-cache-dir -r requirements.txt

exec "$@"
