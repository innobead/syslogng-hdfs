#!/usr/bin/env python
import logging.handlers
import syslog
import socket

logger = logging.getLogger('SyslogLogger')
logger.setLevel(syslog.LOG_INFO)

handler = logging.handlers.SysLogHandler(address=("localhost", 7777), socktype=socket.SOCK_STREAM)
logger.addHandler(handler)

logger.info("Hello world!")
