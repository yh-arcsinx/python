contact ={}
def login():
    print()
    print('新建用户：n/N')
    print('登录账号：e/E')
    print('退出程序：q/Q')
    n = input('请输入指令代码：')
    if n == 'N' or n == 'n':
        name = input('请输入用户名：')
        while not (name not in contact):
            name = input('此用户名已被使用，请重新输入：')
        password = input('请输入密码：')
        contact[name] = password
        print('注册成功，赶紧试试吧')
    if n == 'e' or n == 'E':
        name = input('请输入用户名：')
        while name not in contact:
            name = input('您输入的用户名不存在，请重新输入：')
        password = input('请输入密码：')
        if contact[name] == password:
            print('欢迎进入。。。系统，里面啥也没有！')
        else:
            print('密码错误，请重新登录')
    if n == 'q' or n == 'Q':
        return 2
while 1:
    n = login()
    if n == 2:
        break
        
        
