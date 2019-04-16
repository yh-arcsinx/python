def checkpar(lalala):
    letter = 0
    num = 0
    blank =0
    elsechar = 0
    for each in lalala:
        if each.isalpha():
            letter += 1
        elif each.isdigit():
            num += 1
        elif each == " ":
            blank += 1
        else:
            elsechar += 1
    print('分别是字母 数字 空格 和其他玩意',letter,num,blank,elsechar)
        
