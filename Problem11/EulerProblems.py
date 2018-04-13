# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:49:33 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler Problems 11,16,20,25
 
"""
import numpy as np
import math as m
import time

#########Functions needed for below to solve problems
def sum_nums(strnum):
    #function to sum the digits of a number given an input string
    out_sum_nums=sum(map(int, strnum))
    return(out_sum_nums)
    
def fib_seq(term):
    """
    recursive method is possible but very slow. Code is here for it
    if term==1:
        return(1)
    elif term==2:
        return(1)
    else:
        return(fib_seq(term-1)+fib_seq(term-2))
    """
    # a better approach is to naively add the numbers up since it saves memory unlike the recursive method. might have issues at very large numbers if python does any rounding
    a, b = 0, 1
    for _ in range(term):
        a, b = b, a+b
    return a

#############
    # THis is the implimentation of the most mathematically efficient fibonacci sequence. As I have proven I can code it above I use this in my code for speed purposes
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
##############

#functions for answers to problems
def euler_11():
    #putting 20x20 block into python must be hard coded. Easiest to make a string and then split and convert to integers.
    L = []
    L.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
    L.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
    L.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
    L.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
    L.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
    L.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
    L.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
    L.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
    L.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
    L.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
    L.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
    L.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
    L.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
    L.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
    L.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
    L.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
    L.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
    L.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
    L.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
    L.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
 
    M = [i.split() for i in L]
    M = [[int(j) for j in i] for i in M] 
 
    # there are 20 rows, each containing 20 integers
    max_prod = 0
    
    for i in range(20):
        for j in range(16):
            # right/left products
            prod = M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]
            if prod > max_prod:
                max_prod = prod
            # up/down products
            prod = M[j][i]*M[j+1][i]*M[j+2][i]*M[j+3][i]
            if prod > max_prod:
                max_prod = prod
            
    # diagonal products
    for i in range(16):
        for j in range(16):
            prod = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
            if prod > max_prod: 
                max_prod = prod
    for i in range(3,20): #need to start farther away so anti-diagonal can be made
        for j in range(16):
            prod = M[i][j]*M[i-1][j+1]*M[i-2][j+2]*M[i-3][j+3]
            if prod > max_prod: 
                max_prod = prod
    return(print("Euler Problem 11 answer: {}".format(max_prod)))         

def euler_16():
    num_pow=str(2**1000) #need string since normal int would overflow
    out_16=sum_nums(num_pow)
    return(print("Euler Problem 16 answer: {}".format(out_16)))
    
def euler_20():
    num_fact=str(m.factorial(100))# we implimented factorial in a previous hw so I will call the function
    out_20=sum_nums(num_fact)
    return(print("Euler Problem 20 answer: {}".format(out_20)))
    
def euler_25(k):
    digits=10**k
    t=0
    l=0
    p=6
    while l != digits: #checks if we have the correct amount of digits
        #while loop starts by jumping up in term amount in powers of 10. This allows us to skip large parts of our number space if the term is large. We dont end up checking all the numbers up to that term.
        if l < digits: #checks if we are under and then goes up by a large jump to the next term
            t=t+10**p
            num_fib=str(fibonacci(t))
            l=len(num_fib)
            # we need to check if we have a term with the correct amount of digits but isn't the first term
            if l == digits:
                if l == len(str(fibonacci(t-1))):
                    t=t-10**p
                    p=p-1
                    l=0    
        else: #if the jump was to large we go back to the original term and reduce the jump size
            t=t-10**p
            p=p-1
            l=0 # no need to actually give the length correctly for the term since all we want is the while loop to continue which it will if l=0.
    out_25=t
    return(print("Euler Problem 25 answer: {} This term has 10^{} digits".format(out_25,k)))    
    
euler_11()    
euler_16()
euler_20()
euler_25(3)
#10**6 takes 874.14 seconds
#assume linear model 10**9 takes 962733sec -  267.5 hours