import random as r
legalx=[1,10]
legaly=[1,10]
class Turtle:
    def __init__(self):
        self.power=100
        self.x =r.randint(legalx[0],legalx[1])
        self.y =r.randint(legaly[0],legaly[1])
    def move(self):
        newx = self.x + r.choice([1,2,-1,-2])
        newy = self.y + r.choice([1,2,-1,-2])
        if newx < legalx[0]:
            self.x = 2 * legalx[0] - newx
        elif newx > legalx[1]:
            self.x = 2 * legalx[1] - newx
        else:
            self.x = newx
        if newy < legaly[0]:
            self.y = 2 * legaly[0] - newy
        elif newy > legaly[1]:
            self.y = 2 * legaly[1] - newy
        else:
            self.y = newy
        self.power -= 1
        return(self.x,self.y)
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100
            
class Fish:
    def __init__(self):
        self.x =r.randint(legalx[0],legalx[1])
        self.y =r.randint(legaly[0],legaly[1])
    def move(self):
        newx = self.x + r.choice([1,-1])
        newy = self.y + r.choice([1,-1])
        if newx < legalx[0]:
            self.x = 2 * legalx[0] - newx
        elif newx > legalx[1]:
            self.x = 2 * legalx[1] - newx
        else:
            self.x = newx
        if newy < legaly[0]:
            self.y = 2 * legaly[0] - newy
        elif newy > legaly[1]:
            self.y = 2 * legaly[1] - newy
        else:
            self.y = newy
        return(self.x,self.y)
turtle = Turtle()
fish = []
for i in range(10):
    newfish = Fish()
    fish.append(newfish)

while True:
    if not len(fish):
        print('鱼儿都吃完了，游戏结束！')
        break
    if not turtle.power:
        print('乌龟体力耗尽，挂掉了！')
        break
    pose = turtle.move()
    for eachfish in fish[:]:
        
        if eachfish.move() == pose:
            turtle.eat()
            fish.remove(eachfish)
            print('有一条鱼儿被吃掉了')




#    def start(self,num):
 #       self.num =num
  #      while self.num:
   #         print(self.num)
    #        exec('fish%s ={%d,%d}'%(self.num,random.randint(1,10),random.randint(1,10)))
     #       self.num -= 1



#class turtle:
