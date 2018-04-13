# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:03:25 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler Problem 9. Find pythagorean triplet that solves a+b+c=1000
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

for a in range(1,999):
    for b in range(a,999):
        c=np.sqrt(a**2+b**2)
        if c.is_integer()==True:
            if a+b+c==1000:
                print(a)
                print(b)
                print(c)
                print(a*b*c)