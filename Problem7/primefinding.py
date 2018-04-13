# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:09:27 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler project prime number finding
Currently not efficient. probably an array issue
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

max=10**6

numbers=np.arange(2,max,1)

for ii in numbers:
    if numbers.size == ii:
        break
    else:
        div_value=numbers[ii-2]
        index=[]
        if div_value>numbers.size:
            break
        else:
            for i in range(numbers[ii-2],numbers.size,1):
                if numbers[i]%div_value == 0:
                    if numbers[i] != div_value:
                        index.append(i)
        numbers=np.delete(numbers,index)
if numbers.size>10001:
    print("\a")
    print("enough primes found")
    print(numbers[10000])
    