def returnedread(yeah):
    count = len(yeah)
    i = 0
    flag = 0
    while i < count - 1:
        if yeah[i] == yeah[count - 1]:
            flag = flag + 1
        i = i + 1
        count = count - 1
    if (len(yeah) // 2) == flag:
        print("是回文诗")
    else:
        print("不是回文诗")
