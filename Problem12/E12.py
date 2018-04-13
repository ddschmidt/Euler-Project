# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:02:45 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def natural_num(k):
    t=np.arange(1,k+1)
    return sum(t)

def get_factors(n):    
    return sum(2 for i in range(1, int(round(np.sqrt(n)+1))) if not n % i)

def main():
    j=0
    n=0
    while j<500:
        n=n+1
        num=natural_num(n)
        fac=get_factors(num)
        j=fac
    return natural_num(n)

print(main())