f = open('1.txt')
n = int(input('要几行？:'))
while n > 0:
    n = n - 1
    eachline = f.readline()
    print(eachline,end="")
