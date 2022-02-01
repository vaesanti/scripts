#!/bin/python

import psutil

print(psutil.cpu_percent(interval=1))

#while True:
#    print(psutil.cpu_percent(interval=2))
