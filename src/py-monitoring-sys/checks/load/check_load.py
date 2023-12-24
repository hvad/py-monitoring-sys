#!/usr/bin/env python
# -*- coding: utf-8 -*-


import psutil

def get_load_average():
    """ Get load average."""
    load_avg = psutil.getloadavg()
    return round(load_avg[0],2),round(load_avg[1],2),round(load_avg[2],2)
