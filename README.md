git clone https://github.com/kamlinuxwizard/stepic-web-tech.git /home/box/web
bash /home/box/web/init.sh

*virtualenv*

Устанавливаем pip и virtualenv:

> sudo apt-get update
> sudo apt-get install python3-pip
> sudo pip3 install virtualenv

Создаём новое виртуальное окружение:

> mkdir ~/newproject
> cd ~/newproject
> virtualenv newenv

Если вам нужно будет удалить виртуальное окружение, достаточно сделать rm -rf ~/newproject/newenv/.

Теперь активировать окружение можно с помощью команды запущенной из директории newproject.

> source newenv/bin/activate

Вы увидите, что после этой команды изменится приглашение интерпретатора bash: в начале появится (newenv).

*Django*

Установить Django в виртуальное окружение можно с помощью

> pip install django

в вашем окружении (заметьте, не pip3, несмотря на третий Python!)

Для выхода из окружения используйте команду deactivate (заметьте, она работает только в виртуальном окружении!)

По данным 2 пунктам есть туториал на DigitalOcean (на английском) (https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04).

Создаём Django-проект

> django-admin.py startproject myproject ~/newproject
