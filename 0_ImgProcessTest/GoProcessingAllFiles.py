import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time



oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)





files_ = os.listdir(filesFolderPath)
files = []
for ff in files_:
    if ff.find('.avi') != -1:
        files.append(ff)
        
for FILENAME in files:
    
    fileName = FILENAME.split('.')[0] 
    cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi')) 
    fps = cap.get(cv2.CAP_PROP_FPS) 
    
    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = np.ones((11,11),np.uint8)
    
    
    hh = int(fileName[0:2])
    mm = int(fileName[2:4])
    ss = 30
    
    if hh > 19 and hh < 11:
        judge = 22000        
    else:            
        judge = 15000
    judge = 24000
      
    ii = 0
    data = []
    stPo = []
    endPo = []
    MAXCOUNT = 999999999999
    lastCount = MAXCOUNT
    flag = 0;
    
    try:
        while(cap.isOpened()):
            ret, frame = cap.read()
            ii = ii + 1 
                 
            #road=frame[130:230,250:520] 
            road=frame[120:210,250:520] 
            #road= frame
            fgmask = fgbg.apply(road)                                                  #backgroun
            
            if ii % 25 == 0:
                ss = ss + 1
                
            if ss % 60 == 0 and ss != 0:
                mm = mm + 1
                ss = 0
                
            if mm % 60 == 0:
                hh = hh + 1
                mm = 0 
            
            fgmask = cv2.GaussianBlur(fgmask,(1,1),0)                                  #GaussianBlue
            ret,fgmask = cv2.threshold(fgmask,20,255,cv2.THRESH_BINARY)                #Threshold
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)                  #Morphological transformations-open
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)                 #Morphological transformations-close
             
            
            car = cv2.bitwise_and(road,road,mask = fgmask)                             #get car real images
            
            #### This part is to process figure for catch part
            pcar = cv2.GaussianBlur(car,(1,1),1) 
            #open_cv_img = np.array(pcar) 
            pcar = cv2.cvtColor(pcar,cv2.COLOR_BGR2GRAY) 
        
            fgmask_inv = cv2.bitwise_not(fgmask)                                       #inverse car mask
            white = road.copy() 
            white[:,:] = 255                                                           #make white road background
            road_withoutCar = cv2.bitwise_and(white,white,mask = fgmask_inv)           #road - car_mask
            whiteroad_car = cv2.add(road_withoutCar,car)                               #road + car
            
         
            count = len(np.where(pcar == 0)[0])
            data.append(count)
            print(ii,count,len(stPo),len(endPo),hh,mm,ss)
            
            
            if count < judge:
                flag = flag + 1
            else:
                flag = 0
            
            if ii >= 25 and count < judge and flag >= 10 and lastCount == MAXCOUNT: 
                stPo.append(ii)
                lastCount = count 
                
            if ii >= 25 and  lastCount < judge and count > judge:
                endPo.append(ii)
                lastCount = MAXCOUNT
                
            
            k = cv2.waitKey(20) & 0xff
            if k == 27:
                break
        
    except:
        pass;
    
    
    
        
        
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
    
    
    with open(fileName + '.txt','w') as f:
        for it,ff in enumerate(stPo):
            f.writelines(str(stPo[it]) + ',' + str(endPo[it]) + '\n' )
    
    with open(fileName + '_data.txt','w') as f:
        for ff in data:
            f.writelines(str(ff) + '\n' )
