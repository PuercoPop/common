# -*- coding: utf-8 -*-

from unidecode import unidecode
from django.template import defaultfilters

def u_slugify(value):
    """
    A custom version of slugify that retains non-ascii characters. The purpose 
    of this function in the application is to make URLs more readable in a 
    browser, so there are some added heuristics to retain as much of the title 
    meaning as possible while excluding characters that are troublesome to read 
    in URLs. For example, question marks will be seen in the browser URL as %3F 
    and are thereful unreadable. Although non-ascii characters will also be 
    hex-encoded in the raw URL, most browsers will display them as 
    human-readable glyphs in the address bar -- those should be kept in the 
    slug.
    """
    # remove trailing whitespace
    value = value.strip() 
    # remove spaces before and after dashes
    value = re.sub('\s*-\s*','-', value, re.UNICODE)
    # replace remaining spaces with underscores
    value = re.sub('[\s/]', '_', value, re.UNICODE)
    # replace colons between numbers with dashes
    value = re.sub('(\d):(\d)', r'\1-\2', value, re.UNICODE) 
    # replace double quotes with single quotes
    value = re.sub('"', "'", value, re.UNICODE)
    # remove some characters altogether
    value = re.sub(r'[?,:!@#~`+=$%^&\\*()\[\]{}<>]','',value, re.UNICODE)
    return value

def slugify(value):
    """
    Slugify with better Unicode support
    """
    value = unidecode(value)
    return defaultfilters.slugify(unidecode(value))
