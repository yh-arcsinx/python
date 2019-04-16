#def calculation():
import os
os.chdir('E:\\3DMGAME-Terraria.v1.3.5.3.CHS.Green\\Terraria.v1.3.5.3')
n = os.listdir('.')
dict1 = dict()
for eachfile in n:
    if os.path.isdir(eachfile):
        dict1.setdefault('文件夹', 0)
        dict1['文件夹'] += 1
    else:
        (a,b) = os.path.splitext(eachfile)
        dict1.setdefault(b,0)
        dict1[b] += 1
for eachlist in dict1.keys():
    
    print('该文件夹下有类型为[%s]的文件[%d]个' %(eachlist,dict1[eachlist]))
 
