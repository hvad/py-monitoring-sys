#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil

def detect_disk_names(exclude_names=[], exclude_filesystems=[]):
    """ Discovery disks names."""
    disk_names = []
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.mountpoint != '/' and partition.device not in exclude_names and partition.fstype not in exclude_filesystems:
            disk_names.append(partition.device)
    return disk_names
