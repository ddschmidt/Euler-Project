# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:10:18 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

import itertools
perms=list(itertools.permutations([0, 1, 2,3,4,5,6,7,8,9])) #already sorts into lexicographic order
print(perms[10**6-1])
        
