# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:36:54 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

s=set()
for i in range(1000,0,-1):
    s.add(i**i)
    
print(sum(s))