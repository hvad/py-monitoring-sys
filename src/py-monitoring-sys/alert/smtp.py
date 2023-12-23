#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import argparse
import configparser
import asyncio
from email.message import EmailMessage

# Function to send email alert
async def send_email_alert(subject, message):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    sender_email = config['Email']['Sender']
    receiver_email = config['Email']['Receiver']
    smtp_server = config['Email']['SMTPServer']
    smtp_port = config['Email'].getint('SMTPPort')
    smtp_username = config['Email']['SMTPUsername']
    smtp_password = config['Email']['SMTPPassword']
    
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        await server.send_message(msg)
    finally:
        server.quit()
