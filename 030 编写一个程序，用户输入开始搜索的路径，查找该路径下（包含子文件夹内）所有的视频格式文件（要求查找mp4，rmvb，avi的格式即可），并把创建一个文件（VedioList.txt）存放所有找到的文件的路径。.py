import os
home = 'E:\\python\\fish c\\just for test'
find = 'avi'
f=open(home+'\\jilu.txt','w')
def findavi(home,find):
    os.chdir(home)
    everything = os.listdir()
    for each in everything:
        if os.path.isfile(each):
            (name,ext)=os.path.splitext(each)
     #       print(ext)
            if ext =='.avi':
                f.writelines(each+'在'+os.getcwd()+'\n')
        else:
            findavi(each,find)
            os.chdir(os.pardir)
findavi(home,find)
f.close()
