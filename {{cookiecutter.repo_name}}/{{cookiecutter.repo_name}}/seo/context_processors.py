# -*- coding: utf-8 -*-

from django.conf import settings
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
            page_meta_data = PageMetaData.objects.get(url=request.path)
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
        print('Default meta keywords are missed')
    if not default_page_meta_data.meta_description:
        # TODO log here
        print('Default meta description is missed')
    return {
        'meta_keywords': default_page_meta_data.meta_keywords,
        'meta_description': default_page_meta_data.meta_description
    }
