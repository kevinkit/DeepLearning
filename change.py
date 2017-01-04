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
    for i in range(0,len(predicts),2):
        if mode == 0:
            mean = (predicts[i] + predicts[i+1])/2;
            new[i] = mean;
            new[i + 1] = mean;
        elif mode == 1:
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
                
        else:
            if predicts[i] == predicts[i +1]:
                new[i] = predicts[i];
                new[i +1] = predicts[i+1];
            else:
                #One of them has a class 0 
                mean_ = 1 + (predicts[i] + predicts[i+1])/2;
                new[i] = mean_;
          
        
    return np.asarray(new);
            
all_test_cases = [0,0,1,1,2,2,3,3,4,4,
                  0,1,0,2,0,3,0,4,
                  1,2,1,3,1,4,
                  2,3,2,4,3,4]
            
#z = np.uint8(range(1,5))
#t = np.append(z,z);
#t = np.append(z,t);
t = np.uint8(all_test_cases)


#predicts = np.uint8(5*np.random.rand(6))
n = predict_changer(t,0)



plt.plot(t)
#error_avg = predicts - n;
plt.plot(n)
n1 = predict_changer(t,1)
n2 = predict_changer(t,2)
#plt.plot(n1)
plt.plot(n2)

#heatmap, xedges, yedges = np.histogram2d(t, n1, bins=50)
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plt.clf()
#plt.imshow(heatmap.T, extent=extent, origin='lower')
#cb = plt.colorbar()
#plt.show()

#plt.plot(n1)
#error_lut = predicts - n1
#plt.plot(error_avg)
#plt.plot(error_lut)
