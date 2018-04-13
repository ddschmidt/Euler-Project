# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:36:33 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time    

#%% Euler 30

def euler_30():
    maxN=10**6
    numbers=[]
    for aa in range(11,maxN):
        digits=[int(d) for d in str(aa)]
        s=0
        for ii in digits:
            s=s+ii**5
        if aa==s:
            numbers.append(aa)
    print("Euler 30: Sum total is: {}\nOf the found numbers {}\n".format(sum(numbers),numbers))
    return

euler_30()

#%% Euler 32

def euler_32():
    numbers=set() # we use a set to store our found products so that duplicates are automatically deleted
    for aa in range(1,100):
        for bb in range(1,2000):
            prod=aa*bb
            digits=[]
            digits.append([int(d) for d in str(aa)+str(bb)+str(prod)])
            digits= [y for x in digits for y in x] #flattens the list
            if len(digits)==9 and len(set(digits)-{0})==9: #check if 1-9 pandigital
                numbers.add(prod)

    print("Euler 32: Sum total is: {}\nOf the found numbers {}\n".format(sum(numbers),numbers))
    return

euler_32()