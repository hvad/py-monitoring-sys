#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import time
from core.main import bytes2human

def get_disk_usage(partition):
    disk_usage = psutil.disk_usage(partition)
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

#def check_disk_io():
#    disk_io = psutil.disk_io_counters(perdisk=True)
#    for disk, io in disk_io.items():
#        if disk == '/':
#            read_bytes = io.read_bytes
#            write_bytes = io.write_bytes
#            break
#    else:
#        print("No disk information found for the '/' partition.")
#        return
#    
#    # Wait for 1 second
#    psutil.wait_io_counters()
#    
#    disk_io = psutil.disk_io_counters(perdisk=True)
#    for disk, io in disk_io.items():
#        if disk == '/':
#            read_bytes_diff = io.read_bytes - read_bytes
#            write_bytes_diff = io.write_bytes - write_bytes
#            print(f"Read Bytes: {read_bytes_diff} bytes")
#            print(f"Write Bytes: {write_bytes_diff} bytes")
#            break
#    else:
#        print("No disk information found for the '/' partition.")
