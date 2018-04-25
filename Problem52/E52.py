# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:27:40 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def dignums(n):
    return sorted(list(str(n)))

b=False
n=9999 #start far enough in where we know anything before is bad
while b==False:
    n=n+1
    if dignums(2*n)==dignums(3*n)==dignums(4*n)==dignums(5*n)==dignums(6*n):
        b=True

print(n)
    
    