import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os

oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)
savePath = os.path.join(topPath,thisFolderName)



cap = cv2.VideoCapture(os.path.join(filesFolderPath,'Video.mp4'))


 
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11,11),np.uint8)


for ii in range(150):
        
    
    ret, frame = cap.read()
    
    blur = cv2.blur(frame, (3, 3))
    diff = cv2.absdiff(1080*1920, blur)
    test = diff[:,:,2] 
    ret, thresh = cv2.threshold(test, 115, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite(os.path.join(savePath,'test' + str(ii) + '.png'),thresh)   
    cv2.imwrite(os.path.join(savePath,'test' + str(ii) + 'Ori.png'),frame)   
    if ii == 60:
        oriFig = thresh
    
    

plt.figure()
plt.imshow(frame)
plt.imshow(frame)
plt.figure()
plt.imshow(oriFig)
plt.figure()
plt.imshow(thresh)
plt.figure()
plt.imshow(thresh-oriFig)



# =============================================================================
# ii = 0
# tmp = 0
# while(cap.isOpened()):
#     print(ii)
#     ret, frame = cap.read()
#     # road = frame[475:644,250:1200]
#     ii = ii + 1;
#     if ii == 0:
#         tmp = frame
#         print(ii)
#         break;
# =============================================================================
    
    
    
    
    


# =============================================================================
# =============================================================================
# #     fgmask = fgbg.apply(road)     #backgroun
# #     fgmask = cv2.GaussianBlur(fgmask,(5,5),0) #GaussianBlue
# #     ret,fgmask = cv2.threshold(fgmask,150,255,cv2.THRESH_BINARY)   #Threshold
# #     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)  #Morphological transformations-open
# #     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel) #Morphological transformations-close
# # 
# # 
# #     car = cv2.bitwise_and(road,road,mask = fgmask)  #get car real images
# # 
# #     fgmask_inv = cv2.bitwise_not(fgmask)  #inverse car mask
# #     white=road.copy() 
# #     white[:,:]=255  #make white road background
# #     road_withoutCar = cv2.bitwise_and(white,white,mask = fgmask_inv)  #road -car_mask
# #     whiteroad_car = cv2.add(road_withoutCar,car)  #road + car
# # 
# #     image, contours, hierarchy = cv2.findContours(fgmask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contour
# # 
# #     #print  len(contours)
# #     car_contour1=road.copy()
# #     car_contour1 = cv2.drawContours(car_contour1, contours, -1, (0,255,0), 3)  #draw car contour 
# # 
# #     car_contour2=road.copy()
# #     car_contour3=road.copy()
# #     car_contour4=road.copy()
# #     for i in range(len(contours)):
# #         cnt = contours[i]
# #         M = cv2.moments(cnt)
# #         area = cv2.contourArea(cnt)
# #       
# #         epsilon = 0.1*cv2.arcLength(cnt,True)
# #         approx = cv2.approxPolyDP(cnt,epsilon,True)
# #         car_contour2 = cv2.drawContours(car_contour2, [approx], -1, (0,255,0), 3)  #draw car contour     
# # 
# #         hull = cv2.convexHull(cnt)
# #         car_contour3 = cv2.drawContours(car_contour3, [hull], -1, (0,255,0), 3)  #draw car contour     
# # 
# #         x,y,w,h = cv2.boundingRect(cnt)
# #         car_contour4 = cv2.rectangle(car_contour4,(x,y),(x+w,y+h),(0,255,0),2)
# # 
# # 
# # 
# #     #cv2.imshow('road',road)
# #     cv2.imshow('fgmask',fgmask)
# #     cv2.imshow('car',car)
# #     #cv2.imshow('road_white',whiteroad_car)
# #     #cv2.imshow('car_contour1',car_contour1)
# #     #cv2.imshow('car_contour2',car_contour2)
# #     #cv2.imshow('car_contour3',car_contour3)
# #     cv2.imshow('car_contour4',car_contour4)
# #     #cv2.imshow('carBoundary',carBoundary)
# # 
# # 
# #     k = cv2.waitKey(20) & 0xff
# #     if k == 27:
# #         break
# # cap.release()
# # cv2.destroyAllWindows()
# =============================================================================
# =============================================================================




