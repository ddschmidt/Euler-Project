# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:25:49 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def triangle(n):
    return int(0.5*n*(n+1))

r=1000
triang=np.zeros(r-1)
for i in range(1,r):
    triang[i-1]=triangle(i)
    

f=open("p042_words.txt",'r')
char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
words=sorted(f.read().replace('"','').split(','),key=str)
sumwords=0
for ind,val in enumerate(words):
    temp=0
    for x in val:
        temp+=char_num_dict[x]
    if temp in triang:
        sumwords=sumwords+1
	
print(sumwords)