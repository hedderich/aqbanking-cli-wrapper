import os

from aqbanking import settings


def cache_dir_required(func):
    def cache_dir_wrapper():
        if not os.path.exists(settings.CACHE_PATH):
            os.makedirs(settings.CACHE_PATH)
        return func()
    return cache_dir_wrapper