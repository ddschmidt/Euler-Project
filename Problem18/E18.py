# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:41:21 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
    Collaboration with Joe Gibson on problem
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

a=[[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

for ii in range(13,-1,-1):
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
        