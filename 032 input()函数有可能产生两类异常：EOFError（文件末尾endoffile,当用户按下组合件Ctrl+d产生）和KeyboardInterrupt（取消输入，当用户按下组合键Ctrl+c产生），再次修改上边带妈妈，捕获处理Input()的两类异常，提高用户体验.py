import random

secret = random.randint(1,10)
print('fish C')
try:
    temp = input('不妨猜猜一个数字：')
    guess = int(temp)
except (ValueError,KeyboardInterrupt,EOFError):
    print('输入错误')
    guess = secret
while guess != secret:
    temp = input('诶呀，猜错了，请重新输入吧：')
    guess = int(temp)
    if guess == secret:
        print('厉害了')
    else:
        if guess> secret:
            print('大了大了')
        else:
            print('小了小了')
print('游戏结束！不玩啦！')

