#!/usr/bin/py
import pyautogui as py
from time import sleep

sleep(5)
pic = py.screenshot()
pic.save(r'pic.png')
