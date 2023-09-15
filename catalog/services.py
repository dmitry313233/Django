from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories_from_cache():
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)
    else:
        cache_data = Category.objects.all()
    return cache_data



# def get_cashed_subjects_for_category(product_pk):
#     if settings.CACHE_ENABLED:
#         key = f'subject_list_{product_pk}'
#         product_list = cache.get(key)
#         if product_list is None:
#             product_list = Product.objects.filter(product__pk=product_pk)
#             cache.set(key, product_list)
#     else:
#         product_list = Product.objects.filter(product__pk=product_pk)
#
#     return product_list