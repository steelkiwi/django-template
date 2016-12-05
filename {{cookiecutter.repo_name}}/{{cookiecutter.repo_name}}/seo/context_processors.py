# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings

from django.utils.translation import ugettext as _
from .models import DefaultPageMetaData, PageMetaData


def get_page_meta_data(request):
    """
    Searching and returns keywords and description meta information for given urls.
    """
    if request.method != 'GET':
        return
    url_name = request.resolver_match.url_name if request.resolver_match else None

    if url_name:
        try:
            # TODO cache result here
            page_meta_data = PageMetaData.get_metadata(url=request.path)
            return {
                'meta_keywords': page_meta_data.meta_keywords,
                'meta_description': page_meta_data.meta_description
            }
        except PageMetaData.DoesNotExist:
            return get_default_page_meta_data()


def get_default_page_meta_data():
    default_page_meta_data = DefaultPageMetaData.get_solo()
    if not default_page_meta_data.meta_keywords:
        # TODO log here
        message = _('Default meta keywords are missed')
        warnings.warn(message)
    if not default_page_meta_data.meta_description:
        # TODO log here
        message = _('Default meta description is missed')
        warnings.warn(message)
    return {
        'meta_keywords': default_page_meta_data.meta_keywords,
        'meta_description': default_page_meta_data.meta_description
    }
