# -*- coding: utf-8 -*-

from ordereddict import OrderedDict

def create_error_document(identifier, message):
    """
    Builds an error document formed by an OrderedDict
    composed by an error identifier and error massaged
    """
    result = OrderedDict()
    result['errors'] = []
    error_subdoc = OrderedDict()
    error_subdoc['id'] = identifier
    error_subdoc['message'] = unicode(message)
    result['errors'].append(error_subdoc)
    return result
