# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from solo.models import SingletonModel


class PageMetaDataMixin(models.Model):

    meta_keywords = models.CharField(
        max_length=160, null=True, blank=True,
        help_text=_('Unique coma-separated keywords for this page/item'))
    meta_description = models.CharField(
        max_length=160, null=True, blank=True,
        help_text=_('Short and unique description for this page/item'))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.meta_keywords is not None:
            keywords = self.meta_keywords
            self.meta_keywords = ','.join(
                [k.strip() for k in keywords.split(',') if k.strip()])
        super(PageMetaDataMixin, self).save(*args, **kwargs)


@python_2_unicode_compatible
class DefaultPageMetaData(SingletonModel, PageMetaDataMixin):

    class Meta:
        verbose_name = _('Default Page Meta Data')

    def __str__(self):
        return 'Default Page Meta Data'


@python_2_unicode_compatible
class PageMetaData(PageMetaDataMixin):

    url = models.CharField(
        max_length=200,
        help_text=_('Relative url E.g /home/ or /projects/'),
        unique=True
    )

    class Meta:
        verbose_name = _('Page Meta Data')
        verbose_name_plural = _('Page Meta Data')

    def __str__(self):
        return self.url
