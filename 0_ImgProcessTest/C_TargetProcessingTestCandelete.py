import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os 
  
    
    


# =============================================================================
# data = []
# fileName = '0_Res_p.txt'
# flag = 0
# with open(fileName,'r') as f:
#     data_ = f.readline()
#     while data_ != "": 
#         index = data_.split(' ')
#         if data_.find('**') != -1 or data_.find('--') != -1:
#             data.append(index[0]) 
#         data_ = f.readline(); 
# =============================================================================
        
res = []
data = []
fileName = '0_Res_p.txt'
flag = 0
with open(fileName,'r') as f:
    data_ = f.readline()
    while data_ != "": 
        index = data_.split(' ')
        if flag == 1 and data_.find('_') != -1:
            res.append(data)
            data = []
        if data_.find('_') != -1:
            flag = 0
            
        if data_.find('**') != -1 :
            flag = 1
            data.append(index[0]) 
            
        if flag == 1 and data_.find('--') != -1:
            data.append(index[0]) 
        data_ = f.readline(); 
 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        