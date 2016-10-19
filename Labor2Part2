# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:15:44 2016

@author: kevin
"""


import numpy as np
import matplotlib.pyplot as plt


def myGrid(start,stop,samples):
    if start == stop:
        return;
    #Check the Step size
    stepsize = abs(start-stop)/(float(samples) -1)
    vals = np.arange(start,abs(stop-start) + stepsize,abs(start-stop)/(float(samples) -1));
    
    len_val = len(vals)
    #horrible but fast hack
    if vals[-1] > stop:
        vals = vals[0:len_val-1];
    
    len_val = len(vals)   
    n = samples*len_val;
    x = np.zeros(n*2);     
    s = x.reshape(n,2);
    
    for i in range(0,len_val):
        s[i*len_val:(i+1)*len_val,1] = vals[i];
        s[i*len_val:(i+1)*len_val,0] = vals;   
    

    return s
    
#Execute func here
xy = myGrid(-1,1,3); #3 Werte auf 3 --> Stepsize 1
print xy
xy = myGrid(0,1,5)   #5 Werte auf 2
print xy;


if xy != None:
    plt.scatter(xy[:,0],xy[:,1]);
