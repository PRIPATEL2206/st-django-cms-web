#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install psycopg2
pip install gunicorn

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi