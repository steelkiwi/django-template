Usage
-----
Run next commands::

    $ pip install cookiecutter

    $ cookiecutter git@git.steelkiwi.com:moiseenko/new_project.git

    $ vagrant up

    $ vagrant ssh

    $ cd vagrant

    $ sudo pip install -U pip setuptools

    $ sudo pip install -r requirements/local.txt

    $ sudo -u postgres createuser -s vagrant

    $ createdb {{ project_name }} -E=UTF8 --locale=en_US.utf8 --template=template0

    $ python manage.py migrate --settings=config.settings.local

    $ python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

