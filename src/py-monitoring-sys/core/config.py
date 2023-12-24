#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    '''
    Environment variables class
    '''
    PROJECT_NAME: str = "Python System Monitoring"
    PROJECT_VERSION: str = "0.0.1"

settings = Settings()

def validate_configuration(config):
    """ Validate configuration file."""
    required_sections = ["Settings", "Load"]
    required_keys = {
        "Settings": ["check_period", "enable_log", "logfile_name"],
        "Load": ["enable"],
        "Disks": ["enable", "warning","critical"],
        "Memory": ["enable", "warning","critical"],
        "Network": ["enable", "name"],
        "NTP": ["enable", "ntp_pool_server"],
        "Email": ["Sender", "Receiver", "SMTPServer", "SMTPPort", "SMTPUsername", "SMTPPassword"]
    }

    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section: {section}")
        for key in required_keys[section]:
            if key not in config[section]:
                raise ValueError(f"Missing required key: {key} in section: {section}")
