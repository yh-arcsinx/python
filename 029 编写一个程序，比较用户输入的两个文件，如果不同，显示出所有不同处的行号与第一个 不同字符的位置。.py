
def bijiao():
    f1 = open('1.txt')
    f2 = open('2.txt')
    count = 0
    sum_line = []
    for each1 in f1:
        count = count + 1
        each2 = f2.readline()
        if not each1 in each2:
            sum_line.append(count)
    f1.close()
    f2.close()
    return sum_line
sumline = bijiao()
print(sumline)
    
