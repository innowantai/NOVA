import numpy as np


fileName = '11550002_mpeg4.txt' 







def GetTimes():    
    hh = int(fileName[0:2])
    mm = int(fileName[2:4]) 
    ss = 30
    oriss = hh * 60 * 60 + mm * 60 + ss 

def timeTrans(sec):
    ss = np.round(sec % 60)
    mm = np.floor(sec/60)
    hh = np.floor(mm/60)
    mm = mm % 60
    res = [int(hh),int(mm),int(ss)]
    return res
    
    


stPo = []
endPo = []
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
        diff.append(index3)
        res = timeTrans(index1 / 25 + oriss)
        stTimes.append( str(res[0]) + ':' + str(res[1])  + ':' + str(res[2]-2))
        res = timeTrans(index2 / 25 + oriss)
        endTimes.append( str(res[0]) + ':' + str(res[1])  + ':' + str(res[2]))

print(stTimes)
print(endTimes)
    
    
    
