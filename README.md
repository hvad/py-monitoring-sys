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

Log

Alert 

Discovery disks


## How to install


## How to configure

Configuration file example : 
```
[Settings]
check_period=60
logfile_name=std.log
logfile_days=7

[Load]
enable=True

[Disks]
enable=True
warning=80
critical=90

[Memory]
warning=90
enable=True
critical=98

[Network]
enable=True
name="lo"

[Email]
Sender = your_email@example.com
Receiver = recipient_email@example.com
SMTPServer = smtp.example.com
SMTPPort = 587
SMTPUsername = your_username
SMTPPassword = your_password
```

```
$ python main.py -c config.ini 
```
