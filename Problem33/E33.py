# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:30:15 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import math

frac=[1,1]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if (i*10+j)/(j*10+k)==i/k and i!=k:
                gcd=math.gcd(i,k)
                frac[0]=frac[0]*i/gcd
                frac[1]=frac[1]*k/gcd

gcd=math.gcd(int(frac[0]),int(frac[1]))
frac[0]=frac[0]/gcd
frac[1]=frac[1]/gcd
print(frac[1])