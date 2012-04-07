# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

def tag_flow_urls(tag):
    urls = {}
    urls['todos'] = reverse("tag_view", kwargs={'tag': tag.tag}) +\
        "?flow=todos"
    urls['destacados'] = reverse("tag_view", kwargs={'tag': tag.tag}) +\
        "?flow=destacados"
    urls['mimula'] = reverse("tag_view", kwargs={'tag': tag.tag}) +\
        "?flow=mimula"
    urls['portada'] = reverse("tag_view", kwargs={'tag': tag.tag})
    return urls

def homepage_flow_urls():
    urls = {}
    urls['todos'] = reverse("homepage_view") + "?flow=todos"
    urls['destacados'] = reverse("homepage_view") + "?flow=destacados"
    urls['mimula'] = reverse("homepage_view") + "?flow=mimula"
    urls['portada'] = reverse("homepage_view")
    return urls
