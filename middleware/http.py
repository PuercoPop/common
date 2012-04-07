# -*- coding: utf-8 -*-
"""
   HTTP 403 catch middleware.
"""
from os.path import join

from django.conf import settings
from django.contrib.sites.models import Site
from django.template import RequestContext, loader

FORBIDDEN_TEMPLATE = '403.html'

class HttpHandler(object):
    """
    This middleware should grab HttpResponseForbidden requests and 
    use a 403.html template to display its contents.
    """

    def process_response(self, request, response):
        """
            Handle HttpResponseForbidden responses and use the appropiate
            tempalte to display the message.
        """
        if response.status_code == 403:    
            content = response.content
            sites = {
                str(settings.APTITUS_SITE_ID): 'aptitus',
                str(settings.TUMAX_SITE_ID): 'tumax',
                str(settings.NEOAUTO_SITE_ID): 'neoauto'
            }
            try:
                site_name = sites[str(Site.objects.get_current().id)]
            except KeyError:
                # Some new undefined site
                site_name = ''

            template = loader.get_template(join(site_name, FORBIDDEN_TEMPLATE))
            response.content = template.render(RequestContext(request, {
                'message': content
            }))
        return response
