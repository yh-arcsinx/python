
def creat_new():
    title = input('请输入文件名:')
    f = open(title +'.txt','x')
    inside = input('请输入内容【单独输入"w"保存并退出】：\n')
    while not (inside == 'w'):
        f.writelines(inside + '\n')
        inside = input()
    f.close()

creat_new()
