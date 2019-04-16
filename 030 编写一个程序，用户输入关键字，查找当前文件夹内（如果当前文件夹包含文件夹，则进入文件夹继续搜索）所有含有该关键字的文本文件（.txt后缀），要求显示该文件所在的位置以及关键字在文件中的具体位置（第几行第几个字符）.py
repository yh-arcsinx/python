import os
home = 'E:\\python\\fish c\\just for test'
find = 'a'
def findinside(home,find):
    os.chdir(home)
    listall = os.listdir()
    for each in listall:
        if os.path.isfile(each):
            (name,ext)=os.path.splitext(each)
            if ext == '.txt':
                f=open(each)
                count = 0
                for eachline in f:
                    count += 1
                    if find in eachline:
                        print(each,os.getcwd(),'在第%d行'%count)
                f.close()
        elif os.path.isdir(each):
            findinside(each,find)
            os.chdir(os.pardir)


findinside(home,find)
