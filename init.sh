#!/usr/bin/env bash

USER="box"
# USER="firstuser"

sudo ln -s /home/$USER/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# sudo ln -s /home/$USER/web/etc/hello.py /etc/gunicorn.d/hello.py
# sudo ln -s /home/$USER/web/etc/django.py /etc/gunicorn.d/django.py
# sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -u root -e "create database ask"
mysql -u root -e "CREATE USER 'ask'@'localhost' IDENTIFIED BY 'poX-1eema';"
mysql -u root -e "GRANT ALL PRIVILEGES ON ask.* To 'ask'@'localhost'"
