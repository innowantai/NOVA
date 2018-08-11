import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time


def loadData(fileName):    
    
    data = []
    with open(fileName,'r') as f:
        data_ = f.readline()
        while data_ != "":
          data.append(int(data_))
          data_ = f.readline();
    return data

    
def timeTrans(sec):
    ss = np.round(sec % 60)
    mm = np.floor(sec/60)
    hh = np.floor(mm/60)
    mm = mm % 60
    res = [int(hh),int(mm),int(ss)]
    return res
    
def GetTimes(fileName):   
    hh = int(fileName[0:2])
    mm = int(fileName[2:4]) 
    ss = 30
    oriss = hh * 60 * 60 + mm * 60 + ss  
    
    stPo = []
    endPo = []
    iters = []
    with open(fileName,'r') as f:
        data = f.readline()
        while data != "":
          stPo.append(int(data.split(',')[0]))
          endPo.append(int(data.split(',')[1]))
          data = f.readline();
          
    
    diff = []
    stTimes = []
    endTimes = []
    for it,ff in enumerate(stPo):
        index1 = stPo[it]
        index2 = endPo[it]
        index3 = (index2 - index1) / 25 
        if index3 >= 2:
            iters.append(it)
            diff.append(index3)
            res = timeTrans(index1 / 25 + oriss)
            stTimes.append( str(res[0]) + ':' + str(res[1])  + ':' + str(res[2]-2))
            res = timeTrans(index2 / 25 + oriss)
            endTimes.append( str(res[0]) + ':' + str(res[1])  + ':' + str(res[2]))
    return stTimes,endTimes,iters,stPo,endPo
    print(stTimes)
    print(endTimes)




files_ = os.listdir()
files = []
Datas = []
for ff in files_:
    if ff.find('_data.txt') != -1:
        files.append(ff)
        Datas.append(loadData(ff))
        
        
        

target = 0
STTIMES = []
ENDTIMES = []
RESULTS = []
for target in range(len(Datas)):     
    data = Datas[target]
    filename = files[target]    
    stTimes_ , endTimes_, iters, stPo, endPo = GetTimes(filename.replace('_data',''))
    
    RESULTS.append(filename.split("_data")[0])    
    for ii, _ in enumerate(stTimes_):
        index = str(iters[ii]) + " : " + stTimes_[ii] + "  " + endTimes_[ii] + " " + str(stPo[iters[ii]]) + " " + str(endPo[iters[ii]]) + " " + str(endPo[iters[ii]]-stPo[iters[ii]])
        RESULTS.append(index)
    RESULTS.append(" ")

with open('0_Res.txt','w') as f:
    for rr in RESULTS:
        f.writelines(rr + '\n')
    


#### 15








