import math

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def input(self):
        (self.x,self.y) = input(':').split()
        self.x = int(self.x)
        self.y = int(self.y)
    def get(self):
        return (self.x,self.y)
class Line():
    def __init__(self,p1,p2):
        self.x = (p1.get())[0] - (p2.get())[0]
        self.y = (p1.get())[1] - (p2.get())[1]

    def len(self):
        self.len = math.sqrt(self.x*self.x+self.y*self.y)
        print(self.len)
    

        
