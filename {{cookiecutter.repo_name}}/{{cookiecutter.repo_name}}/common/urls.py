# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import HealthCheckView


urlpatterns = [
    url(r'^checker/$', HealthCheckView.as_view()),
]