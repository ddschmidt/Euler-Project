# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:24:37 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import itertools

digs=[1,2,3,4,5,6,7,8,9]   
pantup=list(itertools.permutations(digs))

def tup2int(n):
    s=0
    for i in range(len(n)):
        s=s+n[i]*10**(len(n)-i-1)
    return s

pannums=set()
for kk in pantup:
    pannums.add(tup2int(kk))

pansmade=set()
for ii in range(1,30000):
    concatprod=''
    for jj in range(1,100):
        concatprod=concatprod+str(ii*jj)
        if len(list(concatprod))>9:
            break
        if int(concatprod) in pannums:
            pansmade.add(int(concatprod))
    
print(max(pansmade))
