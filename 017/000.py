def power(x,y):
    s = 1
    if y <= 0:
        return 0
    
    while y:
        s = s * x
        y = y - 1
    return s
        
