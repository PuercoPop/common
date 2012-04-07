""" Threadlocals middleware and related functions.
"""
from django.contrib.auth.models import AnonymousUser

from common.app.users.utils import get_cached_user

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_user():
    """ Get the logged User object from locals. Sometimes it can return an
    AnonymousUser.
    """
    user = getattr(_thread_locals, 'user', None)
    if user is None:
        user = get_cached_user(1)
    return user

def get_non_anonymous_user():
    """ Get the logged User object from locals. Sometimes there is no logged
    user so we get the admin user.
    """
    user = getattr(_thread_locals, 'user', None)
    if (user is None) or (isinstance(user, AnonymousUser)):
        user = get_cached_user(1)
    return user

class ThreadLocals(object):
    """ Middleware that gets various objects from the request object and saves
    them in thread local storage.
    """
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)
