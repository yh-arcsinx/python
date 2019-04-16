def shuixianhua():
    i = 100
    while i < 1000:
        g = i % 10
        s = i // 10
        b = s // 10
        s = s % 10
        if i == g**3 + s**3 + b**3:
            print(i)
        i = i + 1
