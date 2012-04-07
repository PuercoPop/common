# -*- coding: utf-8 -*-
"""
Utilities for the registration app. Basically Cache Stuff.
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache

from common.app.users.constants import CACHE_USER

def get_cached_user(user_id):
    """ Gets a User object from the Cache, or try to get it from the DB, or
    return a None object if it does not exist. Receives the User Id as the
    parameter.
    """
    user = cache.get(CACHE_USER % (settings.SITE_ID, user_id), None)
    if user is None:
        try:
            user = User.objects.get(pk=user_id)
            cache.set(CACHE_USER % (settings.SITE_ID, user_id), user,
                      settings.DEFAULT_CACHE_TIMEOUT)
        except User.DoesNotExist:
            user = None
    return user
