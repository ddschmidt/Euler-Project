# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:31:35 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

dec="0"
for i in range(1,1000000):
    dec=dec+str(i)

dec=list(dec)

prod=1
for k in range(7):
    prod=prod*int(dec[10**k])
    
print(prod)