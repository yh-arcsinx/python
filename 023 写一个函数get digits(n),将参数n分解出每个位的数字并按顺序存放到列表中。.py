mix = []
def get_digits(n):
 #   global mix
    if n > 0:
        mix.insert(0,n % 10)
        get_digits(n//10)

    else:
        return 0
n = int(input("haha:"))
get_digits(n)
print(mix)
