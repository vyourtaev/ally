#!/bin/bash
python3 /opt/apps/code/manage.py makemigrations
python3 /opt/apps/code/manage.py migrate
python3 /opt/apps/code/manage.py collectstatic --noinput

#touch /opt/apps/log/gunicorn.log
#touch /opt/apps/log/gunicorn-access.log
#tail -n 0 -f /opt/apps/log/*.log &
#
#
#echo Starting Gunicorn.
#exec gunicorn ally.wsgi:application \
#    --name ally \
#    --bind 0.0.0.0:5005 \
#    --workers 3 \
#    --log-level=info \
#    --log-file=/opt/apps/log/gunicorn.log \
#    --access-logfile=/opt/apps/log/gunicorn-access.log \
#    "$@"
#
