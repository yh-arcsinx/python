num = int(input("请输入一个整数："))
while num:
    num1 = num
    while num1:
        print(" ",end = "")
        num1 = num1 - 1
    num1 = num
    while num1:
        print("*",end = "")
        num1 = num1 - 1
    print()
    num = num - 1
