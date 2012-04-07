# -*- coding: utf-8 -*- 

import time 
import hashlib
from django.utils.http import http_date, quote_etag

def etag_from_value(request, value, add_quotes=False):
    if value is None:
        return None
    result = hashlib.sha1(request.path + str(value)).hexdigest()
    if add_quotes:
        result = quote_etag(result)
    return result

#FIXME: Delete when no other part of the coded uses this functions
def response_add_last_modified(response, last_modified):
    """
    Adds the Last-Modified HTTP header to the given response
    based on a datetime value passed as a parameter.
    """
    last_modified = http_date(
        time.mktime(last_modified.timetuple())
    )
    response['Last-Modified'] = last_modified
    return response

def response_add_etag(response, etag):
    """
    Adds the ETag HTTP header to the given response based on
    an arbitrary text string passed as a parameter.
    """
    response['ETag'] = etag
    return response

def response_add_last_modified_and_etag(request, response, last_modified):
    """
    Adds the Last-Modified and ETag HTTP headers to the given
    response based on a datetime value passed as a parameter 
    and the request path.
    """
    response = response_add_last_modified(response, last_modified)
    etag = quote_etag(hashlib.sha1(request.path + str(last_modified)).hexdigest())
    response = response_add_etag(response, etag)
    return response
