import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time



def ImageProcess_sub(frame,ii,ss,mm,hh):
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
    
    fgmask = cv2.GaussianBlur(fgmask,(3,3),0)                                  #GaussianBlue
    ret,fgmask = cv2.threshold(fgmask,20,255,cv2.THRESH_BINARY)                #Threshold
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)                  #Morphological transformations-open
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)                 #Morphological transformations-close
             
    car = cv2.bitwise_and(road,road,mask = fgmask)                             #get car real images        
   
    pcar = cv2.GaussianBlur(car,(5,5),1)                                       #### This part is to process figure for catch part
    #open_cv_img = np.array(pcar) 
    pcar = cv2.cvtColor(pcar,cv2.COLOR_BGR2GRAY) 

    #fgmask_inv = cv2.bitwise_not(fgmask)                                       #inverse car mask
    white = road.copy() 
    white[:,:] = 255                                                           #make white road background
    #road_withoutCar = cv2.bitwise_and(white,white,mask = fgmask_inv)           #road - car_mask
    #whiteroad_car = cv2.add(road_withoutCar,car)                               #road + car    


    image, contours, hierarchy = cv2.findContours(fgmask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contour   
    car_contour1=road.copy()
    car_contour1 = cv2.drawContours(car_contour1, contours, -1, (0,255,0), 3)  #draw car contour 
    #car_contour2=road.copy()
    #car_contour3=road.copy()
    car_contour4=road.copy()
    for i in range(len(contours)):
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        car_contour4 = cv2.rectangle(car_contour4,(x,y),(x+w,y+h),(0,255,0),2)
    return car,pcar,car_contour4,ss,mm,hh
    
    

oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)


fileName = '04250035_mpeg4'
### D  12250003_mpeg4
### N  23250025_mpeg4
#cap = cv2.VideoCapture(os.path.join(filesFolderPath,'06250039_mpeg4'  + '2_Split' +'.avi'))
cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi'))
#cap = cv2.VideoCapture(os.path.join(filesFolderPath,'train'  +'.avi'))
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
  
ii = 0
data = []
stPo = []
endPo = []
MAXCOUNT = 999999999999
lastCount = MAXCOUNT
flag = 0;

try:
    while(cap.isOpened()):
        ii = ii + 1 
        ret, frame = cap.read()
    
        car,pcar,car_contour4,ss,mm,hh = ImageProcess_sub(frame,ii,ss,mm,hh)
    
    
        cv2.imshow('car',car)
        cv2.imshow('pcar',pcar)
        cv2.imshow('car_contour4',car_contour4)
        
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




jghhgj

with open(fileName + '.txt','w') as f:
    for it,ff in enumerate(stPo):
        f.writelines(str(stPo[it]) + ',' + str(endPo[it]) + '\n' )

with open(fileName + '_data.txt','w') as f:
    for ff in data:
        f.writelines(str(ff) + '\n' )


# =============================================================================
#         M = cv2.moments(cnt)
#         area = cv2.contourArea(cnt)      
#         epsilon = 0.1*cv2.arcLength(cnt,True)
#         approx = cv2.approxPolyDP(cnt,epsilon,True)
#         car_contour2 = cv2.drawContours(car_contour2, [approx], -1, (0,255,0), 3)  #draw car contour     
#         hull = cv2.convexHull(cnt)
#         car_contour3 = cv2.drawContours(car_contour3, [hull], -1, (0,255,0), 3)    #draw car contour     
# =============================================================================











    #cv2.imshow('road',road)
    #cv2.imshow('fgmask',fgmask)    
    #cv2.imshow('road_white',whiteroad_car)
    #cv2.imshow('car_contour1',car_contour1)
    #cv2.imshow('car_contour2',car_contour2)
    #cv2.imshow('car_contour3',car_contour3)
    #cv2.imshow('carBoundary',carBoundary)
