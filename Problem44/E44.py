# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:43:05 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def pent(n):
    return int(n*(3*n-1)/2)

#pentlist=[]
#for i in range(1,10000):
#    pentlist.append(pent(i))
def E44():   
    pentset=set()
    i=1000
    while True:
        i+=1
        p1=pent(i)
        for kk in pentset:
            if p1-kk in pentset and p1-2*kk in pentset:
                return(p1-2*kk)
        pentset.add(p1)
    
print(E44())