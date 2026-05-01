#!/bin/bash

echo "Starting dev environment..."

docker-compose up -d db redis

poetry run alembic upgrade head

poetry run uvicorn app.main:app --reload