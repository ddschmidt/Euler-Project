# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:12:54 2018
@author: ddsch (Python 3.6)
David Schmidt

Description:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

day30m=[4,6,9,11]
dayslist=["m","tu","wed","th","fr","sat","sun"]

def Sundays():
    sundaycount=0
    daysum=0
    sunlist=[]
    testlist=[]
    for year in range(1900,2001):
        for month in range(1,13):
            if month in day30m:
                days=30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days = 29
                else:
                    days = 28
            else:
                days=31
#            for ii in range(1,days+1):
#                testlist=testlist+[year,month,ii,dayslist[(ii%7-1)]]            
            if (daysum+1)%7==0 and year!=1900:
                sundaycount=sundaycount+1
                sunlist=sunlist+[year,month]
            daysum=daysum+days
    print(sundaycount)
    return(sunlist)
x=Sundays()