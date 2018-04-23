# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:36:56 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
    Increasing amount is the same as the example. not sure if that was meant to be known but most people say it is
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy
import itertools

t=list(sympy.sieve.primerange(1488, 10**4))
x=set(t)

def is_perm(a,b): 
    return sorted(str(a))==sorted(str(b))

for i in t:
    if i+3330 in x and i+6660 in x:
        a=i
        b=i+3330
        c=i+6660
        if is_perm(a,b) and is_perm(a,b):
            print(a,b,c)