def shuru(a ='1:7'):
   # print(type(a))
  #  print(a)
    (begin,end) = a.split(':')
   # print(begin,end)
    b = int(begin)-1
    while b:
        b = b-1
        f.readline()
    while int(end) >= int(begin):
        begin = int(begin) + 1
        eachline = f.readline()
        print(eachline,end="")
  #  print(begin,end)
        
f = open('1.txt')
n = input('要几行？:')
if n=='':
    shuru()
else:
    shuru(n)
f.close()
