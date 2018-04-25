# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:56:21 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def d(n):
    facs={1}
    fsum=0
    for i in range(2,int(np.sqrt(n))):
        if n%i==0:
            facs.add(i)
            facs.add(int(n/i))
            fsum=sum(facs)
    return fsum

amsum=0   
for i in range(1,10000):
    if i==d(d(i)) and i!=d(i):#perfect numbers don't count(aka if d(i)=i then of course d(d(i))=i but the pair is i and i which is not a pair)
        amsum=amsum+i
    
       
print(amsum)
        