# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
    {% raw %}# Django Admin, use {% url 'admin:index' %}{% endraw %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^users/', include("{{ cookiecutter.repo_name }}.users.urls", namespace="users")),
    url(r'^common/', include("{{ cookiecutter.repo_name }}.common.urls", namespace="common")),
    {%- if cookiecutter.use_allauth == 'y' %}
    url(r'^accounts/', include('allauth.urls')),
    {%- endif %}
    {%- if cookiecutter.use_robots == 'y' %}
    url(r'^robots\.txt', include('robots.urls')),
    {%- endif %}
    # Your stuff: custom urls includes go here
]

if settings.USE_SILK:
    urlpatterns += [
        url(r'^silk/', include('silk.urls', namespace='silk'))
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
