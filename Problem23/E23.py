# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Code base from:
    http://firsttimeprogrammer.blogspot.com/2015/07/the-heat-equation-python-implementation.html
"""
import numpy as np

def abundant(n):
    facs={1}
    fsum=0
    for i in range(2,int(np.sqrt(n))+1):
        if n%i==0:
            facs.add(i)
            facs.add(int(n/i))
            fsum=sum(facs)
            if fsum>n:
                return True
    return False
    
ablist=set()
        
s=set()
for i in range(28123):
    if abundant(i):
        ablist.add(i)
    if not any( (i-a in ablist) for a in ablist ):
        s.add(i)

print(sum(s))