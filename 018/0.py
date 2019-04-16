def mifen(*param):
    i = len(param)
    base = 3
    sum = 0
    if param[i-1] == 5:
        base = 5
    for each in param:
        sum = each + sum
    sum = sum * base
    return sum
