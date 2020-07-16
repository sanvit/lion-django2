#!/bin/bash

python manage.py makemigrations
python manage.py migrate
#uwsgi --http :8000 --module lion.wsgi --enable-threads
uwsgi --http :8000 --module lion.wsgi --enable-threads --static-map /static=`pwd`/static