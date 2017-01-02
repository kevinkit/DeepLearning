# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 11:49:44 2017

@author: Kevin
"""

import numpy as np
import matplotlib.pyplot as plt


#mode = 0 --> mean
#mode = 1 --> non linear LUT
def predict_changer(predicts,mode=0):
       
        
    new = np.empty(predicts.shape)
    for i in range(0,len(predicts)-1,2):
        if mode == 0:
            mean = (predicts[i] + predicts[i+1])/2;
            new[i] = mean;
            new[i + 1] = mean;
        else:
            #Both are the same, so simple copy 
            if predicts[i] == predicts[i +1]:
                new[i] = predicts[i];
                new[i +1] = predicts[i+1];
            else:
                #One of them has a class 0 
                mean = (predicts[i] + predicts[i+1])/2;
                if predicts[i] == 0 or predicts[i+1] == 0:
                    if mean >= 3:
                        new[i] = 3;
                        new[i +1] = 3;
                    else:
                        new[i] = 0;
                        new[i +1] = 0;
                else:
                    if predicts[i] == 1 or predicts[i+1] == 1:
                        if mean >= 3:
                            new[i] = 3;
                            new[i +1] = 3;
                        else:
                            new[i] = 1;
                            new[i +1] = 1;
                    else:
                        if predicts[i] == 2 or predicts[i+1] == 2:
                            if mean >= 3:
                                new[i] = 3;
                                new[i +1] = 3;
                            else:
                                new[i] = 2;
                                new[i +1] = 2;
                        else:
                            if predicts[i] == 3 or predicts[i+1] == 3:
                                if mean >= 3:
                                    new[i] = 4;
                                    new[i +1] = 4;
                                else:
                                    new[i] = 2;
                                    new[i +1] = 2;     
                            else:
                                if predicts[i] == 4 or predicts[i+1] == 4:
                                    if mean >= 3:
                                        new[i] = 4;
                                        new[i +1] = 4;
                                    else:
                                        new[i] = 3;
                                        new[i +1] = 3;    
                
            
    return np.asarray(new);
            
            
        
        


predicts = np.uint8(5*np.random.rand(6))
n = predict_changer(predicts,0)
plt.plot(predicts)
error_avg = predicts - n;
plt.plot(n)
n1 = predict_changer(predicts,1)
plt.plot(n1)
error_lut = predicts - n1
plt.plot(error_avg)
plt.plot(error_lut)
