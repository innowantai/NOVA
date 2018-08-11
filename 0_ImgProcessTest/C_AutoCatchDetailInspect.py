import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time


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

def ImageProcess_sub(road,frame,ii,blur):
    #road= frame
    fgmask = fgbg.apply(road)                                                  #backgroun
    
    
    fgmask = cv2.GaussianBlur(fgmask,(blur,blur),1)                                  #GaussianBlue
    ret,fgmask = cv2.threshold(fgmask,20,255,cv2.THRESH_BINARY)                #Threshold
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)                  #Morphological transformations-open
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)                 #Morphological transformations-close
             
    car = cv2.bitwise_and(road,road,mask = fgmask)                             #get car real images        
   
    pcar = cv2.GaussianBlur(car,(1,1),1)                                       #### This part is to process figure for catch part
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
    return car,pcar,car_contour4,fgmask,contours
    
    
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

def loadData(fileName):    
    
    data = []
    with open(fileName,'r') as f:
        data_ = f.readline()
        while data_ != "":
          data.append(int(data_))
          data_ = f.readline();
    return data


oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)

 
fileName = '04250035_mpeg4'
cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi'))
fps = cap.get(cv2.CAP_PROP_FPS)
st, end = loadStEnd(fileName + '.txt')
resData = loadData(fileName + '_data.txt')

#### 22250023_mpeg4 2 火車

checkTarget = 0

fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11,11),np.uint8)
hh = int(fileName[0:2])
mm = int(fileName[2:4])
ss = 30

if hh >= 19 or hh < 11:
    judge = 22000        
else:            
    judge = 15000

judge = 24000
  
ii = 0
flag = 0;
data = []
stPo = []
endPo = []
MAXCOUNT = 999999999999
lastCount = MAXCOUNT


blur = 1

try:
    while(cap.isOpened()):
        ii = ii + 1 
        ret, frame = cap.read()
        #road=frame[130:230,250:520] 
        #road = frame    
        
        ss,mm,hh = timesCount(ss,mm,hh,ii)
        if ii >= st[checkTarget] - 100 :#and ii <= end[checkTarget]:   
            road=frame[120:210,250:520]   
            car,pcar,car_contour4,fgmask,contours = ImageProcess_sub(road,frame,ii,blur)          
            count = len(np.where(pcar == 0)[0])
            data.append(count)          
            cv2.imshow('car',car)
            cv2.imshow('pcar',pcar)
            cv2.imshow('car_contour4',car_contour4)   
             
        
        print(ii,count,len(stPo),len(endPo),hh,mm,ss)  
# =============================================================================
#         if count < judge:
#             flag = flag + 1
#         else:
#             flag = 0
#         
#         if ii >= 25 and count < judge and flag >= 10 and lastCount == MAXCOUNT: 
#             stPo.append(ii)
#             lastCount = count 
#             
#         if ii >= 25 and  lastCount < judge and count > judge:
#             endPo.append(ii)
#             lastCount = MAXCOUNT
# =============================================================================
            
        
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
    
except:
    pass;
 
    
cap.release()
cv2.destroyAllWindows()

 