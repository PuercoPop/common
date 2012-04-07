# -*- coding: utf-8 -*-
"""
Common math utils
"""

def to_base(q, alphabet):
    if q < 0:
        raise ValueError, "must supply a positive integer"
    l = len(alphabet)
    converted = []
    while q != 0:
        q, r = divmod(q, l)
        converted.insert(0, alphabet[r])
    return "".join(converted) or '0'

def to32(q):
    """
    Returns a encoded string for a given number.
    It adds an offset to ensure there is a decent sized result
    """
    offset = 10000000
    return to_base(offset + q, '4agf2hkve3prq7stu9jmnyzwx5b6d8c')
