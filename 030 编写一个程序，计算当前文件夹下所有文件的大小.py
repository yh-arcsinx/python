def size(home = 'E:\\3DMGAME-Terraria.v1.3.5.3.CHS.Green\\Terraria.v1.3.5.3'):
    import os
    os.chdir(home)
    listhome = os.listdir('.')
    for each in listhome:
        print(each,'【%dB】'%os.path.getsize(each))
home = input('请输入一个绝对路径:')
if home == '':
    size()
else:
    size(home)
