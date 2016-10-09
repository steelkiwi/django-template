Установка зависимостей
======================
Для установки проекта вам понадобится Vagrant, VirtualBox, cookiecutter, git.
Проверьте установлены ли данные компоненты.
Если нет то установите их.

Установка VirtalBox
===================
Скачайте последнюю версию с сайта Virtualbox https://www.virtualbox.org/wiki/Downloads
Или воспользуйтесь пакетным менеджером

### Linux:

* ``$ sudo apt-get update``
* ``$ sudo apt-get install virtualbox``
* ``$ sudo apt-get install virtualbox-dkms``

### Mac OS:

* ``$ brew cask install virtualbox``

Установка Vagrant
=================

### Linux:

Не пытайтесь устанавливать vagrant из официальных репозиториев ОС (либо сравните версию доступную в репо с версией указанной на официальном сайте) https://www.vagrantup.com/downloads.html

* ``$ sudo apt-get update``
* ``$ sudo apt-get install nfs-utils nfs-utils-lib``

Если последнее не работает

* ``$ sudo apt-get install nfs-kernel-server``
* ``$ sudo apt-get install nfs-common``
* ``$ sudo service nfs-kernel-server start``

### Mac OS:

Скачайте последнюю версию с сайт Vagrant: https://www.vagrantup.com/downloads.html

Или установите с помощью homebrew и cask:

* ``$ brew cask install vagrant``

### Установка cookiecutter

* ``$ sudo pip install -U cookiecutter``

### Установка ansible

* ``pip install --upgrade paramiko PyYAML Jinja2 httplib2 six ansible==2.0.1.0``

### Установка Git

Следуйте инструкциям на https://git-scm.com/book/en/v1/Getting-Started-Installing-Git

### Linux:

* ``$ sudo apt-get install git``

### Mac OS:

* ``$ brew install git``

### Установка проекта, настройка, конфигурация

Загрузка шаблонного проекта
Для загрузки шаблонного проекта используем cookiecutter, выполните следующую команду:

* ``$ cookiecutter git@git.steelkiwi.com:web/django-template.git``

Далее следуйте инструкциям в командной строке.

Шаблон включает в себя в том числе конфигурацию ansible, выберите необходимые для проекта роли.

### Запуск проекта

Для запуска проекта выполните команды:

* ``$ vagrant up``
* ``$ vagrant ssh``
* ``$ cd /vagrant``
* ``$ cp env.example ./config/.env``
* ``$ python manage.py runserver 0.0.0.0:8000``

### Инициализация Git

После того как проект был сконфигурирован, нам необходимо инициализавроать git репозиторий, добавить соответствующий удаленный сервер и выполнить первый коммит с загрузкой на удаленный сервер .

Для конфигурации выполните следующие команды:

* ``$ git init``
* ``$ git remote add origin {{ repo_url }}``
* ``$ git add -A``
* ``$ git commit -m "Init commit"``
* ``$ git push origin -u master``