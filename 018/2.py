def findstr(ying):
    a = "You cannnot improve your past, but you can improve your future. Once time is wasted, life is wasted."
    flag = 0
    sum = 0
    for each in a:
        if flag == 0:
            if ying[0] == each:
                flag = 1
            else:
                flag = 0
        else:
            if ying[1] == each:
                sum = sum + 1
            flag = 0
    print(sum)
