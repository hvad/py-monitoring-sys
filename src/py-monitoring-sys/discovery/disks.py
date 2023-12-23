#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import yaml

def get_disk_names(exclude_filesystems=[]):
    disk_names = []
    partitions = psutil.disk_partitions(all=True)
    
    for partition in partitions:
        if partition.fstype not in exclude_filesystems:
            disk_names.append(partition.device)
    
    return disk_names

def write_to_yaml(filename, disk_names):
    config = {'disks': disk_names}
    
    with open(filename, 'w') as file:
        yaml.dump(config, file)

# Usage example
#exclude_filesystems = ['tmpfs']
#disk_names = get_disk_names(exclude_filesystems)
#write_to_yaml('disks.yaml', disk_names)
