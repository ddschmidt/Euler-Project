# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:45:26 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy

def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

def rotate(num, n):
    l=[int(x) for x in str(num)]
    return magic(l[-n:] + l[:-n])


t=list(sympy.sieve.primerange(1, 10**6))
x=set(t)

def main():
    tot=0
    for ii in t:
        ll=len([int(x) for x in str(ii)])
        kk=[ii]
        for jj in range(1,ll):
            kk=kk+[rotate(ii,jj)]
        if all(i in x for i in kk):
           tot=tot+1
    return tot
    
print(main())