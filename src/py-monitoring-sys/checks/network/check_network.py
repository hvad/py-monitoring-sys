#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil


def get_network_interface_state(interface_name):
    stats = psutil.net_if_stats()
    if interface_name in stats:
        return stats[interface_name].isup
    else:
        return False
