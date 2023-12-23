#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil


def get_network_interface_state(interface_name):
    interfaces = psutil.net_if_stats()
    if interface_name in interfaces:
        interface = interfaces[interface_name]
        if interface.isup:
           return (interface_name,isup)
       
    else:
        return False
