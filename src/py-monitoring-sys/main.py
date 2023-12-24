#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import sys
import configparser
import argparse
import daemon

from core.config import settings,validate_configuration
from log.monitoring_log import log_message
from checks.load.check_load import get_load_average
from checks.memory.check_memory import get_memory_usage
from checks.disk.check_disk import get_disk_usage,get_disk_io
from checks.network.check_network import get_network_interface_state
from checks.ntp.check_ntp import check_ntp_sync
from discovery.disks import detect_disk_names


async def sys_get_load_average():
    """ Get load average 1 minute, 5 minutes and 15 minutes."""
    if check_load_enabled:
        load = get_load_average()
        if (load[0] >= float(config['Load']['critical_load1']) or
            load[1]>= float(config['Load']['critical_load5']) or
            load[2]>= float(config['Load']['critical_load15'])): 
            result=f"CRITICAL"
        elif (load[0] >= float(config['Load']['warning_load1']) or
             load[1]>= float(config['Load']['warning_load5']) or
             load[2]>= float(config['Load']['warning_load15'])):
            result=f"WARNING"
        else:
            result=f"OK"

        if settings_log_enabled:
            message=f"{result} - Load average : {load[0]} {load[1]} {load[2]}"
            log_message(config['Settings']['logfile_name'],message)

async def sys_get_memory_usage(warning,critical):
    """ Get memory percent usage."""
    if check_memory_enabled:
        memory = get_memory_usage()
        if  memory >= int(critical):
            result=f"CRITICAL"
        elif memory >= int(warning):
            result=f"WARNING"
        else:
            result=f"OK"
        if settings_log_enabled:
            message=f"{result} - Memory percentage usage : {memory}%"
            log_message(config['Settings']['logfile_name'],message)

async def sys_get_disk_usage(disks):
    """ Get disks usage."""
    if check_disk_enabled:
        list_disks = disks.get('disks', '').split(',')
        for disk in list_disks:
            disk_usage= get_disk_usage(disk)
            if int(disk_usage[3]) >= int(config['Disks']['critical']):
                result=f"CRITICAL"
            elif int(disk_usage[3]) >= int(config['Disks']['warning']):
                result=f"WARNING"
            else:
                result=f"OK"
            if settings_log_enabled:
                message=f"{result} - {disk} Disk percent usage {disk_usage[3]}% Total disk {disk_usage[0]} Used disk {disk_usage[1]}"
                log_message(config['Settings']['logfile_name'],message)

async def sys_get_disk_io():
    """ Get disk I/O."""
    if check_disk_io_enabled and check_disk_enabled:
        disk_io = get_disk_io()
        if settings_log_enabled:
            message=f"Disk I/O Bytes : {disk_io}"
            log_message(config['Settings']['logfile_name'],message)

async def sys_get_network_interface_state(interface_name):
    """ Get network state."""
    if check_network_enabled:
        net = get_network_interface_state(interface_name)
        if net is True:
            result=f"UP"
        else:
            result=f"DOWN"
        if settings_log_enabled:
            message=f"Network : {interface_name} is {result}"
            log_message(config['Settings']['logfile_name'],message)

async def sys_get_ntp_sync(ntp_pool_server):
    """ Get ntp state."""
    if check_ntp_sync_enabled:
        time_sync = check_ntp_sync(ntp_pool_server)
        if time_sync is True:
            result="OK"
        else:
            result="CRITICAL"
        if settings_log_enabled:
            message=f"Time synchonisation is {result}"
            log_message(config['Settings']['logfile_name'],message)

async def run_checks():
    """ Run the checks asynchronously."""
    while True:
        tasks = [
            asyncio.create_task(sys_get_load_average()),
            asyncio.create_task(sys_get_memory_usage(config['Memory']['warning'],config['Memory']['critical'])),
            asyncio.create_task(sys_get_disk_usage(config['Disks'])),
            asyncio.create_task(sys_get_network_interface_state(config['Network']['name'])),
            asyncio.create_task(sys_get_ntp_sync(config['NTP']['ntp_pool_server'])),
            asyncio.create_task(sys_get_disk_io())
        ]
        await asyncio.gather(*tasks)
        await asyncio.sleep(int(config['Settings']['check_period']))  # Add a small delay before running the checks again

def main():
    """ Main function to continuously run the checks."""
    asyncio.run(run_checks())




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--daemon", action="store_true", help="Run as a daemon process")
    parser.add_argument("-c", "--config", required=True, help="Configuration file path")
    parser.add_argument("-A", "--autodiscovery", action="store_true", help="Auto discovery mode")
    args = parser.parse_args()

    if args.config:
        CONFIG_FILE = args.config
    else:
        CONFIG_FILE = "config.ini"

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    # Validate the configuration before starting
    try:
        validate_configuration(config)
    except ValueError as config_file_err:
        print(f"Invalid configuration: {config_file_err}")
        sys.exit(1)

    settings_log_enabled = config.getboolean("Settings","enable_log")
    check_load_enabled = config.getboolean("Load","enable")
    check_disk_enabled = config.getboolean("Disks","enable")
    check_disk_io_enabled = config.getboolean("Disks","io_disk")
    check_memory_enabled = config.getboolean("Memory","enable")
    check_network_enabled = config.getboolean("Network","enable")
    check_ntp_sync_enabled = config.getboolean("NTP","enable")

    if args.daemon:
        with daemon.DaemonContext():
            print(f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION} Started...")
            main()

    elif args.autodiscovery:
        print(f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION} Auto discovery mode")
        exclude_names = []  # Add disk names to exclude, e.g., ['sdb', 'sdc']
        exclude_filesystems = ['devfs']  # Add file system types to exclude, e.g., ['ntfs', 'exfat']
        disk_names = detect_disk_names(exclude_names, exclude_filesystems)
        print(f"Disks discovery : {disk_names}")

    else:
        print(f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION} Started...")
        main()
