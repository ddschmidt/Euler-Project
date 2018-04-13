# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:10:13 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler 41
some number theory math shows the largest prime and pandigital will be 1-7. 8 and 9 not possible
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy

def euler_41():
    num=0
    for ii in list(sympy.sieve.primerange(10**6, 10**7))[::-1]:
        digits=[int(d) for d in str(ii)]
        n=7
        if len(digits)==n and len(set(digits)-{0,8,9})==n: #check if 1-n pandigital
                num=ii
                break
    return (num)
    
print(euler_41())