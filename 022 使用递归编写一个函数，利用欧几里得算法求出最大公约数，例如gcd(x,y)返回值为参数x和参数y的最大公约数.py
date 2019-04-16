def gcd(x,y):
    if y == 0:
        return x
    else:
        c = y
        y = x % y
        x = c
        return gcd(x,y)
num = gcd(1,1)
print(num)
