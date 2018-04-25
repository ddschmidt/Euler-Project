# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:26:32 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy

def right(n):
    plist=list(str(n))
    end=len(plist)
    for j in range(0,end):
        num=''
        for i in range(j,end):
            num=num+plist[i]
        num=int(num)
        if num not in ch:
            return False
    return True

def left(n):
    plist=list(str(n))
    end=len(plist)
    for j in range(0,end):
        num=''
        for i in range(end,j,-1):
            num=num+plist[len(plist)-i]
        num=int(num)
        if num not in ch:
            return False
    return True

t=list(sympy.sieve.primerange(1, 10**6))
ch=set(t)
primes=set()

x=3
while len(primes)<11:
    x=x+1
    ptest=t[x]
    if right(ptest):
        if left(ptest):
            primes.add(ptest)
            print(ptest)
      
print("sum")
print(sum(primes))