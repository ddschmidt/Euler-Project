# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:20:41 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy

t=list(sympy.sieve.primerange(1, 10**4))
x1=list(sympy.sieve.primerange(1, 10**6))
x=set(x1)

nummax=10**6
p_sum=[0]
for i in t:
    p_sum.append(p_sum[-1]+i)
    if p_sum[-1]>= nummax: break
c = len(p_sum)

terms = 1
for i in range(c):
	for j in range(c-1, i+terms, -1):
		n = p_sum[j] - p_sum[i]
		if (j-i > terms and n in x):
			terms, max_prime = j-i, n
			break
        
print(max_prime,terms)