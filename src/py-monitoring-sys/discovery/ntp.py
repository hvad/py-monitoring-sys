#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_chrony_ntp_pool_servers():
    """ Get ntp pool server configuration."""
    servers = []
    with open("/etc/chrony.conf", "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('pool'):
                server = line.split()[1]
                servers.append(server)

    return servers
