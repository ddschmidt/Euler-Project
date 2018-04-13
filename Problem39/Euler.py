# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:22:09 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

#%% Euler 36

def b10tob2pali(n):
    num2=[]
    nc=n
    while nc>0:
        if nc%2==0:
            num2.append(0)
            nc=nc/2
        if nc%2!=0:
            num2.append(1)
            nc,_=divmod(nc,2) # divmod is like % except it gives the remainder and value not just remainder
    if num2==num2[::-1]: # used this logic back in HW 1/2
        return (True,num2[::-1])
    else:
        return (False,num2[::-1])
        
def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True 

def Euler36():
    palinset=set()
    b2set=set()

    for i in range (1, 10**6):
            if isPalindrome(i): # check if palindrome in base 10
                arg,b2num=b10tob2pali(i) # check if palindrome in base 2
                if arg:
                    #print(b2num)
                    palinset.add(i)
    out=sum(palinset)
    #print(palinset)
    #print(b2set)
    return(print("The sum of base 10 and base 2 palindromes under 10**6 is: {}".format(out)))

Euler36()

#%% Euler 39

def Euler39():
    pnum=0
    Mnum=0
    for p in range(12,1001):
        num=0
        for a in range(1,999):
            for b in range(a,999):
                c=np.sqrt(a**2+b**2)
                if c.is_integer()==True:
                    if a+b+c==p:
                        num=num+1
        if num>Mnum:
            Mnum=num
            pnum=p
            
    print((pnum,Mnum))
# my method was very slow so I started looking online for simplifications. Some of the easiest ones include limiting the parameter space we need to look at.
    #p can only ever be even due to the equations being used
    #a only needs to be evaluated to p/2+sqrt(2)
    #This last one is the real speed help
    #we can refumulate the c condition to instead be a condition on b with a known a and p. This really cuts down on parameter space since we only need to iterate over a and p insted of a p and b. We essentially use the two equations to reduce the number of variables
    
    #Insight from https://blog.dreamshire.com/project-euler-39-solution/
def Euler39_fast():
    pnum=0
    Mnum=0
    for p in range(12,1001,2):
        num=0
        alim=int(p/(2+np.sqrt(2)))+1
        for a in range(1,alim):
            b=p*(p-2*a)/(2*(p-a))
            if b.is_integer()==True:
                num=num+1
        if num>Mnum:
            Mnum=num
            pnum=p
            
    print("A perimeter of {} gives the most solutions at {}".format(pnum,Mnum))
    
Euler39_fast()
