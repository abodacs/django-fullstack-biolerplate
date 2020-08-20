#!/usr/bin/env bash
set -e

echo "Launching command: $@ ..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER online_benevolent;
    CREATE DATABASE online_benevolent_dev;
    GRANT ALL PRIVILEGES ON DATABASE online_benevolent_dev TO online_benevolent;
EOSQL
