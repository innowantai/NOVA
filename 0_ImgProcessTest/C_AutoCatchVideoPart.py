import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os 


def timesCount(ss,mm,hh,ii):
    if ii % 25 == 0:
        ss = ss + 1            
    if ss % 60 == 0 and ss != 0:
        mm = mm + 1
        ss = 0            
    if mm % 60 == 0 and mm != 0:
        hh = hh + 1
        mm = 0
    return ss,mm,hh

def loadStEnd(fileName):   
    st = []
    end = []
    with open(fileName,'r') as f:
        data_ = f.readline()
        while data_ != "":
          st.append(int(data_.split(',')[0]))
          end.append(int(data_.split(',')[1]))
          data_ = f.readline();
    return st,end


def initTimes(fileName):
    hh = int(fileName[0:2])
    mm = int(fileName[2:4])
    ss = 30
    return hh, mm, ss
    

def CatchingTargetVideo(targets):   
    ii = 0 
    ll = len(targets) - 1
    hh, mm, ss = initTimes(fileName)
    checkTarget = targets[1]
# =============================================================================
#     try:
# =============================================================================
    shHeadPoint = 0
    while(cap.isOpened()):
        ii = ii + 1 
        ret, frame = cap.read()
        ss,mm,hh = timesCount(ss,mm,hh,ii)
        
            
        for po in range(ll): 
            target = targets[po + 1] 
            if ii == st[target] - shHeadPoint :
                saveName = os.path.join(saveFolderPath,fileName + '_' + str(target)  + "_" + str(st[target]) + '.avi')
                fourcc = cv2.VideoWriter_fourcc(*'DIVX')
                out = cv2.VideoWriter(saveName, fourcc, 25.0, (640, 480))
                checkTarget = target
                break
            
         
        if ii >= st[checkTarget] - shHeadPoint :#and ii <= end[checkTarget]: 
            print(ii)
            out.write(frame)
            #cv2.imshow('frame',frame)   
            
        if ii >= end[checkTarget] : #st[checkTarget] + 2000  : 
            out.release()
        
        if ii >= st[targets[-1]]+2000:
            break
        print(ii,hh,mm,ss)  
        
        
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
         
# =============================================================================
#     except: 
#         pass
# =============================================================================
        
    
    

oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)
saveFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName,'ForCheck')
 




Targetss = ( 
        ['18550016_mpeg4',15,20,21,22,29,30,31,33],
        ['22250023_mpeg4',0,1,6],
        ['22550024_mpeg4',1,2],
        )
  
Targets = []
data = []
fileName = '0_Res_p.txt'
flag = 0
with open(fileName,'r') as f:
    data_ = f.readline()
    while data_ != "": 
        index = data_.split(' ')
        if flag == 1 and data_.find('_') != -1:
            Targets.append(data)
            data = []
        if data_.find('_') != -1:
            flag = 0
            
        if data_.find('**') != -1 :
            flag = 1
            data.append(index[0]) 
            
        if flag == 1 and data_.find('--') != -1:
            data.append(int(index[0])) 
        data_ = f.readline(); 
        
        
        

for targets in Targets:
    
    fileName = targets[0]
    cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi'))
    fps = cap.get(cv2.CAP_PROP_FPS) 
    st, end = loadStEnd(fileName + '.txt') 
    
    CatchingTargetVideo(targets)
        


 