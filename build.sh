pip install --upgrade pip


#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py spectacular --file schema.yml
echo yes | python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
