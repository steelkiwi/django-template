#!/bin/bash

echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  apt-key add -
apt-get update
apt-get install -y postgresql-9.4
{% if cookiecutter.use_postgis == "y" %}
# Install postgis
apt-get install postgresql-9.4-postgis-2.1 libgeos-dev
{% endif %}