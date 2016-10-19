# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:55:04 2016

@author: Kevin
"""

import matplotlib.pyplot as plt
import matplotlib.colors as cl
from scipy import misc

#load some images
f = misc.face();
f = misc.imread("unnamed.png");

dims = f.shape;
for i in range(0,dims[2]):  
    plt.imshow(f[:,:,i],'gray');
    plt.show()
    

f = misc.imread("SmilingCat.jpg");

dims = f.shape;
for i in range(0,dims[2]):  
    plt.imshow(f[:,:,i],'gray');
    plt.show()
    
 
#To Hue Saturation Value Room 
hsv = cl.rgb_to_hsv(f);

plt.imshow(hsv);
plt.show()

#Histogram
H = hsv[:,:,1]
n,bins,patches = plt.hist(H)
#May take a while
