#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bytes2human(ndata):
    """ Translate bytes to bits"""
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for inum, symbol in enumerate(symbols):
        prefix[symbol] = 1 << (inum + 1) * 10
    for symbol in reversed(symbols):
        if ndata >= prefix[symbol]:
            value = float(ndata) / prefix[symbol]
            return '%.1f%s' % (value, symbol)
    return "%sB" % ndata
