# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . import models

admin.site.register(models.DefaultPageMetaData, SingletonModelAdmin)


@admin.register(models.PageMetaData)
class PageMetaDataAdmin(admin.ModelAdmin):
    list_display = ('url', 'meta_keywords', 'meta_description')
