#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntplib

def check_ntp_sync(ntp_server_pool):
    try:
        # Connect to the NTP server
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request(ntp_server_pool)

        # Check if the response contains a valid time value
        synchronized = response.offset is not None

        return synchronized
    except ntplib.NTPException:
        return False
