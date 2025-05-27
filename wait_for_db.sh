#!/bin/sh
# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

until python -c "import psycopg2; psycopg2.connect(host='$host', user='${POSTGRES_USER}', password='${POSTGRES_PASSWORD}', dbname='${POSTGRES_DB}')" 2>/dev/null; do
  echo "Waiting for postgres at $host..."
  sleep 1
done

exec $cmd
