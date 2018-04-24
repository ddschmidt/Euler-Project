# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:47:41 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import itertools

def tup2int(n):
    s=0
    for i in range(len(n)):
        s=s+n[i]*10**(len(n)-i-1)
    return s
        

#nums=set()
#for i in range(10**9,10**10):
#    if pandig(i):
#        nums.add(i)
#        
digs=[0,1,2,3,4,5,6,7,8,9]   
s=list(itertools.permutations(digs))
divisors=[2,3,5,7,11,13,17]

goodnums=[]
for ii in s:
    if ii[0]!=0:
        for k in range(1,8):
            dig3=ii[k]*100+ii[k+1]*10+ii[k+2]
            if dig3%divisors[k-1]!=0:
                b=False
                break
            else:
                b=True
        if b:
            goodnums.append(ii)

out=0
for k in goodnums:
    out=out+tup2int(k)

print(out)
