# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:54:15 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import math

L=10**6
endsum=0
for i in range(3,L):
    facsum=0
    for k in list(str(i)):
        facsum=facsum+math.factorial(int(k))
    if facsum==i:
        endsum=endsum+i

print(endsum)
    