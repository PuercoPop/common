#! -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def keeptags(value, tags):
    """Strigs all [X]HTML tags except the listed ones"""
    from common.utils.html import keeptags as ktutil
    return mark_safe(ktutil(value, tags))
keeptags.is_safe = True
