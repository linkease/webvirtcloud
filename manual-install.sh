#!/bin/bash

cd /srv/webvirtcloud
cp webvirtcloud/settings.py.template webvirtcloud/settings.py
cp conf/supervisor/webvirtcloud.conf /etc/supervisor/conf.d
cp conf/nginx/webvirtcloud.conf /etc/nginx/conf.d
chown -R www-data:www-data /srv/webvirtcloud
virtualenv -p python3 venv
source venv/bin/activate
pip install -r conf/requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
chown -R www-data:www-data /srv/webvirtcloud
rm /etc/nginx/sites-enabled/default
