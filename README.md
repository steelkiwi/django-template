Dependences installation
========================
For project installation you need Vagrant, VirtualBox, cookiecutter, git.
Check whether these components are installed.
If these components have not installed, please install them.

VirtalBox installation
======================
Download the latest version from the website Virtualbox https://www.virtualbox.org/wiki/Downloads or use the package manager

### Linux:

* ``$ sudo apt-get update``
* ``$ sudo apt-get install virtualbox``
* ``$ sudo apt-get install virtualbox-dkms``

### Mac OS:

* ``$ brew cask install virtualbox``

Vagrant installation
====================

### Linux:

Don't try install vagrant from official OS repositories (or compare the version available in a repo to the version specified on the official site) https://www.vagrantup.com/downloads.html

Then install nfs-utils

* ``$ sudo apt-get update``
* ``$ sudo apt-get install nfs-utils nfs-utils-lib``

If the last doesn't work use these commands

* ``$ sudo apt-get install nfs-kernel-server``
* ``$ sudo apt-get install nfs-common``
* ``$ sudo service nfs-kernel-server start``

### Mac OS:

Download the latest version from Vagran official website: https://www.vagrantup.com/downloads.html

Or install by means of homebrew and cask:

* ``$ brew cask install vagrant``

### Сookiecutter installation

* ``$ sudo pip install -U cookiecutter``

### Ansible installation

* ``pip install --upgrade paramiko PyYAML Jinja2 httplib2 six ansible==2.0.1.0``

### Git installation

Use instruction from https://git-scm.com/book/en/v1/Getting-Started-Installing-Git

### Linux:

* ``$ sudo apt-get install git``

### Mac OS:

* ``$ brew install git``

### Project template installation

For project installation we use cookiecutter. Execute the following command:

* ``$ cookiecutter https://github.com/steelkiwi/django-template.git``

Then follow instructions from command line.

The template includes ansible configuration, choose roles, necessary for the project.

### Start project

* ``$ vagrant up``
* ``$ vagrant ssh``
* ``$ cd /vagrant``
* ``$ cp env.example ./config/.env``
* ``$ python manage.py runserver 0.0.0.0:8000``

### Git inicialisation

* ``$ git init``
* ``$ git remote add origin {{ repo_url }}``
* ``$ git add -A``
* ``$ git commit -m "Init commit"``
* ``$ git push origin -u master``