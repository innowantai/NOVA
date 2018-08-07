import os



FolderName = 'CL303-2' 
fileName = FolderName + '.txt'

def loadData(fileName):    
    data = [];
    with open(fileName,'r') as f:
        ff = f.readline();
        while ff != "":
             data.append(ff)
             ff = f.readline();
    return data;

targets = loadData(fileName)
files = os.listdir(os.path.join(os.getcwd(),FolderName))

         
         
noFiles = [];
okFIles = [];
for target in targets:
    exist = 0
    for ff in files: 
        if ff.find(target[2:-1]) != -1:
            exist = 1
    if exist == 0:
        noFiles.append(target)
    else:
        okFIles.append(target);
    
    
    
print(noFiles)    
    
    
    
    
    
    
    
    
    
    