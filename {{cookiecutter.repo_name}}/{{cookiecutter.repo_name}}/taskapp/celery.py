# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from celery import Celery

from django.apps import AppConfig
from django.conf import settings


if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


app = Celery('{{cookiecutter.repo_name}}')


class CeleryConfig(AppConfig):
    name = '{{cookiecutter.repo_name}}.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        app.config_from_object('django.conf:settings')
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
