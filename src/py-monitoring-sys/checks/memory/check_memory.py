#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil

def get_memory_usage():
    """ Get memory usage in percent."""
    memory_info = psutil.virtual_memory()
    percent = int(memory_info.percent)
    return percent
