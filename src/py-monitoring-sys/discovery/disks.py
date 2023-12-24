#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import configparser

def detect_disk_names(exclude_names=[], exclude_filesystems=[]):
    disk_names = []
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.mountpoint != '/' and partition.device not in exclude_names and partition.fstype not in exclude_filesystems:
            disk_names.append(partition.device)
    return disk_names

#def write_disk_names_to_config(disk_names):
#    config = configparser.ConfigParser()
#    config.read('discovery.ini')
#
#    for i, disk_name in enumerate(disk_names, start=2):
#        section_name = f"Disk{i}"
#        config.set(section_name, "name", disk_name)
#
#    with open('discovery.ini', 'w') as config_file:
#        config.write(config_file)
