# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:46:03 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import math

def Cfunc(n,r):
    out=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return int(out)
    
Ccount=0
for i in range(1,101):
    for j in range(1,i+1):
        if Cfunc(i,j)>10**6:
            Ccount=Ccount+1

print(Ccount)