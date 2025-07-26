#!/bin/sh

echo "Waiting for PostgreSQL at db:5432..."

# Keep checking until PostgreSQL is ready
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL is up. Starting backend..."

# Start your Flask app (or Python backend)
exec python app.py
