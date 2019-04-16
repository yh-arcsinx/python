
def oldyear(n):
    if n > 1:
        return oldyear(n-1) + 2
    else:
        return 10
n = 5
print(oldyear(n))
    
