class Rectangle():
    length = 1
    width = 1
    def setRect(self):
        self.length = float(input('请输入矩形的长和宽..\n长:'))
        self.width = float(input('宽:'))
    def getRect(self):
        print('这个矩形的长是:%.2f,宽是:%.2f' %(self.length,self.width))
    def getArea(self):
        print(self.length*self.width)
        
rect = Rectangle()
    
