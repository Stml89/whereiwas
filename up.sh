#/bin/bash
set -x
set -e

cd /home/whereiwas
git pull --rebase
pip install -r requirements.txt
cd whereiwas
python manage.py migrate