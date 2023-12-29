#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AlertSender:
    def __init__(self, alert_method):
        self.alert_method = alert_method

    def send_alert(self, subject, message):
        self.alert_method(subject, message)
