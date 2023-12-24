#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

def log_message(file_log_name,message):
    """ Simple log function."""
    logging.basicConfig(filename=file_log_name,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(message)
