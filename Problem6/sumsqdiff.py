# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:36:05 2018
@author: ddsch (Python 3.6)

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

a=np.arange(1,101)
b=np.zeros(100)

sumsquared=(a.sum())**2

for i in range(100):
    b[i]=(i+1)**2
    
squaredsum=b.sum()
diff=sumsquared-squaredsum
print(diff)