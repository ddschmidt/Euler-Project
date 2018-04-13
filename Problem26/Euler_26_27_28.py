# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:17:52 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler problems 26, 27, and 28 for Python course
"""
import numpy as np
import sympy
import time

# explanation of this code is in overleaf as the program is really weird. 
# Full reptend prime and ord function explanation
def euler_26():
    for d in list(sympy.sieve.primerange(9*10**4, 10**5))[::-1]:
        period = 1
        while 10**period % d != 1: 
            period += 1
        if d-1 == period: 
            return(print("Euler Problem 26 answer: {}".format(d)))
 
def euler_27():
    primeset=set(sympy.sieve.primerange(0, 10000)) #generate a large set of prime numbers for checking
    nmax=1
    aset=0
    bset=0
    for a in range(-999,1000):# cycle through all and a and b and see how many consecutive primes we make
        for b in range(-1000,1001):
            n=0
            arg=True
            while arg==True:
                x=n**2+a*n+b #make our number
                if x in primeset: #check if in prime set
                    n=n+1
                else: # if not in prime set we see if it is larger then the previous max we found
                    if (n)>nmax: 
                        (nmax,aset,bset)=(n,a,b)
                    arg=False #breaks while loop to allow a and b to change
    return(print("Euler Problem 27 answer: a={}, b={}, Product={}".format(aset,bset,aset*bset)))
    
def euler_28():
    spiral=np.zeros((1001,1001))
    spot=[500,500]
    num=1
    move_dir=0
    move_num=0
    move_max=1
    it=0
    moveset=["right","down","left","up"]
    arg=True
    while arg==True: #generates the spiral by brute force. 
            spiral[spot[0],spot[1]]=num
            num=num+1
            move_num = 1 + move_num
            if moveset[move_dir]=="right":
                spot[1]=spot[1]+1
            if moveset[move_dir]=="down":
                spot[0]=spot[0]+1
            if moveset[move_dir]=="left":
                spot[1]=spot[1]-1
            if moveset[move_dir]=="up":
                spot[0]=spot[0]-1
            if move_num==move_max:
                it=it+1
                move_num=0
                if it==2:
                    move_num=0
                    move_max +=1
                    it=0
                if move_dir==3:
                    move_dir=0
                else:
                    move_dir += 1
            if spot==[0,1000]:
                spiral[spot[0],spot[1]]=num
                arg=False
    diag_sum=np.trace(spiral)+np.trace(spiral[::-1])-1 #takes the trace of each diagonal and subtracts 1 since we double count the center
    return(print("Euler Problem 28 answer: {}".format(diag_sum)))

#tic=time.time()    
euler_26()
#euler_27()
#euler_28()