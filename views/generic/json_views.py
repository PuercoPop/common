# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse

def json_response(request, data, indent=4):
    """
    Serializes data as a JSON document a sends it
    to the web browser
    """
    body = json.dumps(data, indent=4)
    result = HttpResponse(body, mimetype='application/json')
    result['Content-Length'] = len(body)
    return result
