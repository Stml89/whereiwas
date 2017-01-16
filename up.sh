#/bin/bash
set -x
set -e

cd whereiwas
git pull --rebase
pip install -r requirements.txt
cd whereiwas
python manage.py migrate