import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os
import time
import PIL
import scipy.stats as stats


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





def findSquareRande(contours,Input):
    ranges = []
    for i in range(len(contours)):
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        #print([x,y,w,h])
        if w >= 30 and h >= 30 : #and w != 270 and h != 90 :
            Input = cv2.rectangle(Input,(x,y),(x+w,y+h),(0,255,0),2)
            ranges.append(Input)
    return Input, ranges


def CalculateCorrcoef(stat):
    co = []
    baseCo = stat[0]
    for ss in range(len(stat) - 1):
        co_ = np.corrcoef(baseCo,stat[ss])[0][1]
        co.append(co_)
    #plt.plot(co)
    
    co = co[10:]
    over = np.where(np.array(co) <= 0.9)[0]
    l1 = len(over)
    l2 = len(co)
    ratio = l1 / l2 * 100
    print(ratio)
    
    
    co2 = [] 
    for ss in range(len(stat) - 1):
        co_ = np.corrcoef(stat[ss],stat[ss+1])[0][1]
        co2.append(co_)
    #plt.figure(2)
    #plt.plot(co2)
    co2 = co2[10:]
    over = np.where(np.array(co2) >= 0.8)[0]
    l1 = len(over)
    l2 = len(co)
    ratio2 = l1 / l2 * 100
    print(ratio2) 
    print(ratio > 20 and ratio2 > 20 )
    return ratio,ratio2,co,co2
 


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)
 

def cal_similar(stat):    
    baseSS = stat[0]
    RES1 = []
    for kk in range(len(stat)-1):
        res = cal_corrcoef(baseSS,stat[kk])
        RES1.append(res)
    RES1 = RES1[10:]
    over = np.where(np.array(RES1) <= 0.9)[0]
    l1 = len(over)
    l2 = len(RES1)
    ratio = l1 / l2 * 100
    print(ratio)
        
    
    RES2 = []
    for kk in range(len(stat)-1):
        res = cal_corrcoef(stat[kk],stat[kk+1])
        RES2.append(res)
    RES2 = RES2[10:]
    over = np.where(np.array(RES2) >= 0.7)[0]
    l1 = len(over)
    l2 = len(RES2)
    ratio2 = l1 / l2 * 100
    print(ratio2)
    return ratio,ratio2,RES1,RES2

def cal_corrcoef(m1,m2):
    m1 = np.array(m1).flatten()
    m2 = np.array(m2).flatten()     
    cooo = np.corrcoef(m1,m2)[0][1] 
    return cooo

    
 
def main(fileName):
        
    cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi')) 
    hh = int(fileName[0:2])
    mm = int(fileName[2:4])
    ss = 30
    judge = 24000
    ii = 0
    flag = 0;
    data = []
    stPo = []
    endPo = []
    MAXCOUNT = 999999999999
    lastCount = MAXCOUNT
    blur = 1
    img = []
    try:
        while(cap.isOpened()):
            ii = ii + 1 
            ret, frame = cap.read()
            #road=frame[130:230,250:520] 
            #road = frame    
                
            
            ss,mm,hh = timesCount(ss,mm,hh,ii)   
            #road=frame[160:210,250:520]   
            road=frame[120:210,250:520]   
            car,pcar,car_contour4,fgmask,contours = ImageProcess_sub(road,frame,ii,blur)          
            count = len(np.where(pcar == 0)[0])
            data.append(count)          
            #cv2.imshow('car',car)
            #cv2.imshow('pcar',pcar)
            #cv2.imshow('car_contour4',car_contour4)   
            
            #road_ = cv2.cvtColor(road,cv2.COLOR_BGR2GRAY) 
            if ii == 1: 
                img = road
                baseImg = road
                stat = [] 
                
            if ii >= 1:
                cmpMask = cmpbg.apply(baseImg)
                cmpMask = cmpbg.apply(road) 
                cmpMask = cv2.GaussianBlur(cmpMask,(1,1),1) 
                catch = cv2.bitwise_and(road,road,mask = cmpMask) 
                #po = np.where(res >= 125)
                #res[po] = 0
                #cmpMask = cv2.morphologyEx(cmpMask, cv2.MORPH_CLOSE, kernel) 
                catch = cv2.morphologyEx(catch, cv2.MORPH_CLOSE, kernel) 
                catch = cv2.morphologyEx(catch, cv2.MORPH_OPEN, kernel) 
                #po = np.where(res <= 55)
                #res[po] = 0
                #po = np.where(res != 0)
                #res[po] = 255
                image, contours, hierarchy = cv2.findContours(cmpMask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                #cv2.imwrite(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'),res)
                res2, ranges = findSquareRande(contours,cmpMask.copy())
                
                #plt.imshow(cmpMask)
                cv2.imwrite(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'),road) 
                pilImg = PIL.Image.open(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'))
                pilImg = pilImg.convert('RGB')
                his = pilImg.histogram()
                stat.append(his) 
                #cv2.imshow('pilImg',np.array(pilImg))   
        # =============================================================================
        #         plt.figure(1)
        #         plt.imshow(baseImg)
        #         plt.figure(2)
        #         plt.imshow(road)
        #         plt.figure(3)
        #         plt.imshow(cmpMask)
        #         plt.figure(4)
        #         plt.imshow(res2)
        # =============================================================================
                #break
            
            
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
        cap.release()
        cv2.destroyAllWindows()
    ratio,ratio2,co,co2 = cal_similar(stat)
    return ratio, ratio2
        





CaseTarget = 'OK'


fileName = '11550002_mpeg4_11_26447' 
#fileName = '18550016_mpeg4_33_44398'
#fileName = '18550016_mpeg4_30_43845'

#CaseTarget = 'NG'
fileName = '18550016_mpeg4_31_43921'   ### large bug
#fileName = '18250015_mpeg4_0_3795'

oriPath = os.getcwd()
thisFolderName = os.path.split(oriPath)[1]
topPath = oriPath.split('\\Code')[0]
filesFolderPath = os.path.join(topPath,'RelatedFiles',thisFolderName,'ForCheck',CaseTarget)
saveTestFigure = os.path.join(topPath,'RelatedFiles',thisFolderName,'ForCheck',CaseTarget + "_IMG")
if not os.path.exists(saveTestFigure) :
    os.mkdir(saveTestFigure)

files = os.listdir(filesFolderPath)
 
fileName = files[90].split('.')[0]
# =============================================================================
# r1 = []
# r2 = []
# for ff in files:
#     fgbg = cv2.createBackgroundSubtractorMOG2()
#     cmpbg = cv2.createBackgroundSubtractorMOG2()
#     kernel = np.ones((11,11),np.uint8)
#     fileName = ff.split('.')[0]
#     ratio1 , ratio2  = main(fileName)
#     r1.append(ratio1)
#     r2.append(ratio2)
# =============================================================================
 
  

fgbg = cv2.createBackgroundSubtractorMOG2()
cmpbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11,11),np.uint8)
        
cap = cv2.VideoCapture(os.path.join(filesFolderPath,fileName  +'.avi')) 
hh = int(fileName[0:2])
mm = int(fileName[2:4])
ss = 30
judge = 24000
ii = 0
flag = 0;
data = []
stPo = []
endPo = []
MAXCOUNT = 999999999999
lastCount = MAXCOUNT
blur = 1
img = []
try:
    while(cap.isOpened()):
        ii = ii + 1 
        ret, frame = cap.read()
        #road=frame[130:230,250:520] 
        #road = frame    
            
        
        ss,mm,hh = timesCount(ss,mm,hh,ii)   
        road=frame[160:210,250:520]   
        car,pcar,car_contour4,fgmask,contours = ImageProcess_sub(road,frame,ii,blur)          
        count = len(np.where(pcar == 0)[0])
        data.append(count)          
        cv2.imshow('car',car)
        cv2.imshow('pcar',pcar)
        cv2.imshow('car_contour4',car_contour4)   
        
        #road_ = cv2.cvtColor(road,cv2.COLOR_BGR2GRAY) 
        if ii == 1: 
            img = road
            baseImg = road
            stat = [] 
            allroad = []
            
        if ii >= 1:
            allroad.append(road)
            cmpMask = cmpbg.apply(baseImg)
            cmpMask = cmpbg.apply(road) 
            cmpMask = cv2.GaussianBlur(cmpMask,(1,1),1) 
            catch = cv2.bitwise_and(road,road,mask = cmpMask) 
            #po = np.where(res >= 125)
            #res[po] = 0
            #cmpMask = cv2.morphologyEx(cmpMask, cv2.MORPH_CLOSE, kernel) 
            catch = cv2.morphologyEx(catch, cv2.MORPH_CLOSE, kernel) 
            catch = cv2.morphologyEx(catch, cv2.MORPH_OPEN, kernel) 
            #po = np.where(res <= 55)
            #res[po] = 0
            #po = np.where(res != 0)
            #res[po] = 255
            image, contours, hierarchy = cv2.findContours(cmpMask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            #cv2.imwrite(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'),res)
            res2, ranges = findSquareRande(contours,cmpMask.copy())
            
            #plt.imshow(cmpMask)
            cv2.imwrite(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'),road) 
            pilImg = PIL.Image.open(os.path.join(saveTestFigure,fileName + '_' + str(ii) + '.jpg'))
            pilImg = pilImg.convert('RGB')
            his = pilImg#.histogram()
            stat.append(his) 
            cv2.imshow('pilImg',np.array(pilImg))    
    # =============================================================================
    #         plt.figure(1)
    #         plt.imshow(baseImg)
    #         plt.figure(2)
    #         plt.imshow(road)
    #         plt.figure(3)
    #         plt.imshow(cmpMask)
    #         plt.figure(4)
    #         plt.imshow(res2)
    # =============================================================================
            #break
        
        
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
    cap.release()
    cv2.destroyAllWindows()
    ratio,ratio2,co,co2 = cal_similar(stat)

# =============================================================================
# with open('Ok_r2.txt','w') as f:
#     for ff in r2:
#         f.writelines(str(ff) + '\n')
# 
#     
# 
# =============================================================================


# =============================================================================
# plt.figure(1)
# plt.plot(r1)
# plt.plot(r2)
# plt.figure(2)
# plt.plot(r3)
# plt.plot(r4)
# =============================================================================
plt.figure(1)
plt.plot(co)
plt.plot(co2)
