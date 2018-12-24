#!/usr/bin/env bash

USER="box"
# USER="firstuser"

sudo ln -s /home/$USER/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/$USER/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/$USER/web/etc/django.py /etc/gunicorn.d/django.py
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
