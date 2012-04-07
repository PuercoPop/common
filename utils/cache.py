# -*- coding: utf-8 -*-

import json
import pika

from django.core.cache import cache
from django.utils.hashcompat import md5_constructor
from django.utils.http import urlquote

def template_cache_key(fragment_name, *variables):
    "Devuelve la llave usada por la cache para el fragmento y variable dados."
    args = md5_constructor(u':'.join([urlquote(unicode(v)) for v in variables]))
    cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
    cache_key = cache.make_key(cache_key)
    return cache_key

def invalidate_template_cache(fragment_name, *variables):
    "Borra de cache un fragmento html guardado via la etiqueta cache"
    cache_key = template_cache_key(fragment_name, *variables)
    # cache.delete() no funciona bien
    cache._cache.delete(cache_key)

def invalidate_varnish_url(channel, url="/"):
    "Envía un mensaje a Varnish para invalidar la url especificada."
    channel.exchange_declare(
        exchange='varnish',
        type='fanout',
        durable=True
        )
    message = json.dumps({"url": url})
    channel.basic_publish(exchange='varnish',
                          routing_key='',
                          body=message,
                          properties=pika.BasicProperties(
            delivery_mode = 2, # mensaje persistente
            ))
