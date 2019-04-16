print('欢迎进入通讯录程序')
print('1：查询联系人资料')
print('2：插入新的联系人')
print('3：删除已有联系人')
print('4：退出通讯录程序')
dict1 = dict()
while 1:
    n = int(input('请输入相关的指令代码：'))
    type(n)
    print(n)
    if n == 2:
        name = input('请输入联系人姓名：')
        if name in dict1:
            print('您输入的姓名在通讯录中已经存在 -->',name,num)
            continue
        num = input('请输入用户联系电话：')
        dict1[name] = num
    if n == 1:
        name = input('请输入联系人姓名：')
        dict1[name]
    if n == 3:
        del(dict1[name])
    if n == 4:
        break
print('thanks for your using!')
