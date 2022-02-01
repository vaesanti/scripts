#!/usr/bin/py

import psutil
from gpiozero import CPUTemperature

cpu = CPUTemperature()
while True:    
    print(psutil.cpu_percent(interval=2))
    print(cpu.temperature)