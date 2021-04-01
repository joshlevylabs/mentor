#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace


python mentor/manage.py collectstatic
python mentor/manage.py migrate
python mentor/manage.py runserver 0.0.0.0:8000