# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:18:25 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

nums=set()
for a in range(2,100+1):
    for b in range(2,100+1):
        nums.add(a**b)
        
print(len(nums))