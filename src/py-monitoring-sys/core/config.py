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
    required_sections = ["Settings", "Load"]
    required_keys = {
        "Settings": ["check_period", "enable_log", "logfile_name", "logfile_days"],
        "Load": ["enable"]
    }

    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section: {section}")
        for key in required_keys[section]:
            if key not in config[section]:
                raise ValueError(f"Missing required key: {key} in section: {section}")
