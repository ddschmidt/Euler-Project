# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:23:35 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

def Collatz_term_int(k):
    if k%2==0:
        return int(k/2)
    else:
        return int(3*k+1)
    
def Collatz_term_fl(k):
    if k%2==0:
        return k/2
    else:
        return 3*k+1
    
def main():
    start_num=0
    maxchain=0
    for i in range(56,57):
        chain_len=0
        n=i
        while n!=1:
            chain_len=chain_len+1
            n=Collatz_term_int(n)
        if chain_len>maxchain:
            maxchain=chain_len
            start_num=i
    return (start_num,maxchain)
        
print(main())