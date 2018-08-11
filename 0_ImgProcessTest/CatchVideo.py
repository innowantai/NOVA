import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time



oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName)


fileName = '06250039_mpeg4.avi'

cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName))

 
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11,11),np.uint8)

 # 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter(os.path.join(filesFolderPath,fileName.split('.')[0] + '2_Split' + '.avi'), fourcc, 25.0, (640, 480))

## train 3200
## train2 3200
## trainN 31000
ii = 0;
cat = 4000
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    ii = ii + 1;
    print(ii)
   
    
    if ii >= cat:
        out.write(frame)
        cv2.imshow('frame',frame)
    if ii >= cat+2000:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

#DIVX、XVID、MJPG、X264、WMV1、WMV2 等，使用時可以自己嘗試看看。

# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()