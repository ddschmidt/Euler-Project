# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:52:59 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def digitsum(n):
    out=0
    for i in list(str(n)):
        out=out+int(i)
    return(out)
    
numset=set()
for a in range(1,101):
    for b in range(1,101):
        num=a**b
        numset.add(digitsum(num))
        
print(max(numset))