# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:37:21 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def tri(n):
    return int(n*(n+1)/2)

def pent(n):
    return int(n*(3*n-1)/2)

def hexa(n):
    return int(n*(2*n-1))

hset=set()
for i in range(144,10**6):
    hset.add(hexa(i))

pset=set()
for i in range(166,10**6):
    pset.add(pent(i))
    
for i in range(286,10**6):
    num=tri(i)
    if num in pset and num in hset:
        print(num)
        break
