import os
import numpy as np
import matplotlib.pyplot as plt


def loadData(fileName):    
    
    data = []
    with open(fileName,'r') as f:
        data_ = f.readline()
        while data_ != "":
          data.append(int(data_))
          data_ = f.readline();
    return data


files = []
files_ = os.listdir()
for ff in files_:
    if ff.find('_data') != -1:
        files.append(ff)
        
        
target = 12
data = loadData(files[target])
judge = np.mean(data)
data[0] = 0
for i,_ in enumerate(data):
    if data[i] == 0 or data[i] >= judge*0.9:
        data[i] = 0


resPo = []
for i in range(len(data)-1):
    if data[i+1]-data[i] != 0:
        resPo.append(i)
        
     