#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import sys
import configparser
import argparse
import logging
import daemon

from core.config import settings
from log.monitoring_log import setup_logging
from checks.load.check_load import get_load_average
from checks.memory.check_memory import get_memory_usage
from checks.disk.check_disk import get_disk_usage,get_disk_io
from checks.network.check_network import get_network_interface_state


async def sys_get_load_average():
    """ Get load average 1 minute, 5 minutes and 15 minutes."""
    if check_load_enabled:
        load = get_load_average()
        logging.info(f"Load : {load}")

async def sys_get_memory_usage(warning,critical):
    """ Get memory percent usage."""
    if check_memory_enabled:
        memory = get_memory_usage()
        if  memory >= int(critical):
            logging.info(f"CRITICAL - Memory percentage usage : {memory}%")
        elif memory >= int(warning):
            logging.info(f"WARNING - Memory percentage usage : {memory}%")
        else:
            logging.info(f"OK - Memory percentage usage : {memory}%")

async def sys_get_disk_usage(partition):
    """ Get disk usage."""
    if check_disk_enabled:
        disk_usage_all = get_disk_usage(partition)
        logging.info(f"Disk Usage : {disk_usage_all}")

async def sys_get_disk_io():
    """ Get disk I/O."""
    if check_disk_enabled:
        disk_io = get_disk_io()
        logging.info(f"Disk I/O Bytes : {disk_io}")

async def sys_get_network_interface_state(interface_name):
    """ Get network state."""
    if check_network_enabled:
        net = get_network_interface_state(interface_name)
        logging.info(f"Network : {net}")

async def run_checks():
    """ Run the checks asynchronously."""
    setup_logging(config['Settings']['logfile_name'],config['Settings']['logfile_days'])
    while True:
        tasks = [
            asyncio.create_task(sys_get_load_average()),
            asyncio.create_task(sys_get_memory_usage(config['Memory']['warning'],config['Memory']['critical'])),
            asyncio.create_task(sys_get_disk_usage("/")),
            asyncio.create_task(sys_get_network_interface_state(config['Network']['name'])),
            asyncio.create_task(sys_get_disk_io())
        ]
        await asyncio.gather(*tasks)
        await asyncio.sleep(int(config['Settings']['check_period']))  # Add a small delay before running the checks again

def validate_configuration(config):
    required_sections = ["Settings", "Load"]
    required_keys = {
        "Settings": ["check_period", "logfile_name", "logfile_days"],
        "Load": ["enable"]
    }

    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section: {section}")
        for key in required_keys[section]:
            if key not in config[section]:
                raise ValueError(f"Missing required key: {key} in section: {section}")


def main():
    """ Main function to continuously run the checks."""
    asyncio.run(run_checks())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--daemon", action="store_true", help="Run as a daemon process")
    parser.add_argument("-c", "--config", required=True, help="Configuration file path")
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
    except ValueError as e:
        print(f"Invalid configuration: {e}")
        exit(1)

    check_load_enabled = config.getboolean("Load","enable") 
    check_disk_enabled = config.getboolean("Disks","enable") 
    check_memory_enabled = config.getboolean("Memory","enable") 
    check_network_enabled = config.getboolean("Network","enable") 

    if args.daemon:
        with daemon.DaemonContext(stderr=sys.stderr):
            print(f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION} Started...")
            main()
    else:
        print(f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION} Started...")
        main()
