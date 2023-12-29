# Python 3 Linux Monitoring System


## Description

Python tool to monitoring linux system. 

## Features

Check configuration file before start

Check load average

Check memory usage

Check disk usage

Check NTP drift/sync

Check firewall change and specific rules

Check SSL Certificate expired

Stats disk I/O

Stats network I/O

Log checks and stats in file.

Alert when thresolds 

Discovery disks and ntp configuration.


## How to install

Git clone repository

Create a python 3 virtual environnment

Install python 3 requirements

## How to configure

Configuration file example : 
```
[Settings]
check_period=60
enable_log=True
enable_alert=True
logfile_name=std.log

[Load]
enable=True
warning_load1=2
critical_load1=4
warning_load5=4
critical_load5=6
warning_load15=6
critical_load15=8

[Disks]
enable=True
io_disk=True
warning=85
critical=95
disks=/,/var

[Memory]
enable=True
warning=90
critical=98

[Network]
enable=True
name=en0

[NTP]
enable=True
ntp_pool_server=3.pool.ntp.org

[Email]
Sender = your_email@example.com
Receiver = recipient_email@example.com
SMTPServer = smtp.example.com
SMTPPort = 587
SMTPUsername = your_username
SMTPPassword = your_password
```

Execute command below for daemon mode : 
```
$ python main.py -c config.ini -d
```

Execute command below for console mode : 
