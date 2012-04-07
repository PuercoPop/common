# -*- coding: utf-8 -*-

def import_path(name):
  (mod,mem) = name.rsplit('.',1)
  m = __import__(mod, fromlist=[mem])
  return getattr(m, mem)
