#!/bin/sh

if ["$DATABASE"="postgres"]
then
echo "waiting for postgresql..."
 while ! nc -z $SQL_HOST $SQL_PORT ; do
    slep  1.0
 done 
 echo 'PostgreSQL started'

fi

 python3 manage.py flush --no-input

 python3 manage.py migrate

exec "$@"