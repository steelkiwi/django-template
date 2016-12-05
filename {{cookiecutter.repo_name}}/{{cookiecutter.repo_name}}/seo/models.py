# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.cache import cache
from django.conf import settings

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

    @classmethod
    def get_metadata(cls, url=None):
        if url is None:
            raise cls.DoesNotExist(
                "%s matching query does not exist." %
                cls._meta.object_name
            )
        cache_name = '{}_{}'.format(cls._meta.object_name.lower(), url.strip().replace(' ', '').replace('/', '_'))

        cache_obj = cache.get(cache_name)
        if not cache_obj:
            cache_timeout = getattr(settings, 'PAGE_META_DATA_CACHE_TIMEOUT', 600)
            cache_obj = cls.objects.get(url=url)
            cache.set(cache_name, cache_obj, cache_timeout)
        return cache_obj