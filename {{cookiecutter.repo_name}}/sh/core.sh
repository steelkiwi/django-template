#!/bin/bash

apt-get update
# Install build tools
apt-get install -y git build-essential postgresql-server-dev-all libxml2-dev libxslt1-dev libevent-dev libffi-dev

#Install pillow dependency
apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
