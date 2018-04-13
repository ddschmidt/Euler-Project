# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:39:50 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

#This is a statisitical problem. No need to do any crazy calculations since this is the exact reason the binomial coefficient was made. For an nxn grid we will use the binomial coefficient (2n n) to find how many paths are available

def Binomial(n):
    coeff= np.math.factorial(2*n)/(np.math.factorial(n))**2
    return coeff

print(Binomial(20))