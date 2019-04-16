def bin11(num):
    if num == 1:
        print("0b",end="")
    else:
        bin11(num//2)
    print(num % 2,end="")
num = int(input("二进制转换，输入一个数："))
bin11(num)
