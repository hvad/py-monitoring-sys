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
