#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AlertSender:
    """ Class to send alert."""
    def __init__(self, alert_method):
        self.alert_method = alert_method

    def send_alert(self, subject, message):
        """ send alert with method"""
        self.alert_method(subject, message)
