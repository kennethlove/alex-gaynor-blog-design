#!/usr/bin/env python

# Borrowed from
# https://github.com/kennethlove/liquidluck-theme-moment/blob/master/filters.py


def description(key):
    from liquidluck.options import settings
    dct = settings.theme['vars'].get('descriptions')
    if not isinstance(dct, dict):
        return ''
    if key not in dct:
        return ''
    return dct[key]
