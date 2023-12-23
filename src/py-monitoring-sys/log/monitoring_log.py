#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging(file_log_name,days):
    logging.basicConfig(level=logging.INFO)
    handler = TimedRotatingFileHandler(file_log_name, when='midnight', backupCount=days)
    handler.setLevel(logging.INFO)
    handler.suffix = "%Y-%m-%d.log"
    handler.extMatch = r"^\d{4}-\d{2}-\d{2}.log$"
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger('').addHandler(handler)
