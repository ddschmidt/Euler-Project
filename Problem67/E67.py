# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:17:12 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
    
with open('p067_triangle.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
            
a=polyShape
for ii in range(98,-1,-1):
    #print(a[ii])
    rownew=[]
    for jj in range(1,len(a[ii+1])):
        basenum=a[ii][jj-1]
        #print(basenum)
        num1=a[ii+1][(jj-1)]+basenum
        num2=a[ii+1][jj]+basenum
        #print(num1,num2)
        maxnum=max(num1,num2)
        rownew.append(maxnum)
    a[ii]=rownew
    print(a[ii])