import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time



oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)



cap = cv2.VideoCapture(os.path.join(filesFolderPath,'trainN.avi'))

 
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11,11),np.uint8)

## train 3200
## trainN 31000
  
ii = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    ii = ii + 1
    print(ii)
     
    if ii >= 31000:     
        
        #road=frame[225:500,200:350]
        #road=frame[220:500,100:350]
        #road=frame[0:500,0:500]
        #oad=frame[200:500,100:350] 
        road= frame
        fgmask = fgbg.apply(road)                                                  #backgroun
        
        
        fgmask = cv2.GaussianBlur(fgmask,(3,3),0)                                  #GaussianBlue
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
    
        image, contours, hierarchy = cv2.findContours(fgmask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contour
    
        
        
        car_contour1=road.copy()
        car_contour1 = cv2.drawContours(car_contour1, contours, -1, (0,255,0), 3)  #draw car contour 
    
        car_contour2=road.copy()
        car_contour3=road.copy()
        car_contour4=road.copy()
        for i in range(len(contours)):
            cnt = contours[i]
            M = cv2.moments(cnt)
            area = cv2.contourArea(cnt)
          
            epsilon = 0.1*cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,epsilon,True)
            car_contour2 = cv2.drawContours(car_contour2, [approx], -1, (0,255,0), 3)  #draw car contour     
    
            hull = cv2.convexHull(cnt)
            car_contour3 = cv2.drawContours(car_contour3, [hull], -1, (0,255,0), 3)    #draw car contour     
    
            x,y,w,h = cv2.boundingRect(cnt)
            car_contour4 = cv2.rectangle(car_contour4,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    
        #cv2.imshow('road',road)
        #cv2.imshow('fgmask',fgmask)
        cv2.imshow('car',car)
        cv2.imshow('pcar',pcar)
        #cv2.imshow('road_white',whiteroad_car)
        #cv2.imshow('car_contour1',car_contour1)
        #cv2.imshow('car_contour2',car_contour2)
        #cv2.imshow('car_contour3',car_contour3)
        cv2.imshow('car_contour4',car_contour4)
        #cv2.imshow('carBoundary',carBoundary)
        print(len(contours))
        time.sleep(0)
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
    
    
    
cap.release()
cv2.destroyAllWindows()
