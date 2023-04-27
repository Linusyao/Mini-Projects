# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:31:53 2023

@author: Linusyao
"""


import pyautogui as pag
import random 
import time

while True:
     x=random.randint(600,700)
     y=random.randint(200,600)
     pag.moveTo(x,y,0.5)
     time.sleep(2)
     