# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:36:01 2018
@author: ddsch (Python 3.6)
David Schmidt

Description: Euler 10
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import sympy

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

print(sum(primes_sieve(2*10**6)))