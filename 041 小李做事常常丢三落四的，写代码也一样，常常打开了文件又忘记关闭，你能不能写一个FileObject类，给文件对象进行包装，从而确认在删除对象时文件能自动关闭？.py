class FileObject:
    """确认删除对象时，文件可以自动关闭"""
    def __init__(self,filename='OpenMe.txt'):
        self.new=open(filename,'r+')
    def __del__(self):
        self.new.close()
        
