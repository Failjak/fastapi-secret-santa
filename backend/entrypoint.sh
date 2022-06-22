#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then

    echo "Waiting for PostgreSQL"

    while ! nc -z $POSTGRES_SERVER $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

alembic upgrade head
uvicorn main:app --host 0.0.0.0 --port 8008 --reload

exec "$@"