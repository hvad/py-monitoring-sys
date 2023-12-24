#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import time
from core.main import bytes2human

def get_disk_usage(disk):
    disk_usage = psutil.disk_usage(disk)
    disk_usage_total = bytes2human(disk_usage.total)
    disk_usage_used = bytes2human(disk_usage.used)
    disk_usage_free = bytes2human(disk_usage.free)
    disk_usage_percent = disk_usage.percent
    return disk_usage_total,disk_usage_used,disk_usage_free,disk_usage_percent

def get_disk_io():
    disk_io = psutil.disk_io_counters()
    read_bytes = disk_io.read_bytes
    write_bytes = disk_io.write_bytes
    time.sleep(1)  # Wait for 1 second
    disk_io = psutil.disk_io_counters()
    read_bytes_diff = disk_io.read_bytes - read_bytes
    write_bytes_diff = disk_io.write_bytes - write_bytes
    return read_bytes_diff,write_bytes_diff
