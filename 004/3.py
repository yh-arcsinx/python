import random
times = 3

secret = random.randint(1,10)

while times:
    guess = int(input("猜一个数 吧:"))
    times = times - 1
    if guess == secret:
        times = 0
        print("恭喜你猜对了！")
    if guess < secret:
        print("诶呀，猜小了")
    if guess > secret:
        print("诶呀，猜大了")
print("游戏结束啦！")
    
