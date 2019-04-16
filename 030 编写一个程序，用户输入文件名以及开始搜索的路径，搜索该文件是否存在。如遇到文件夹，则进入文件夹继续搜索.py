import os
home = 'E:\\python\\fish c\\just for test'
find = 'aba.txt'
def searching(home,find):
    os.chdir(home)
    searchlist = os.listdir()
    if find in searchlist:
        print('这个%s文件在%s里' %(find,os.getcwd()))
    else:
  #      print(searchlist)
        for eachdir in searchlist:
  #          print(eachdir)
  #          print(searchlist)
            if os.path.isdir(eachdir):
                searching(eachdir,find)
  #          else:
   #             print('我是张')
                os.chdir(os.pardir)
        
searching(home,find) 
