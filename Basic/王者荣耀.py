# 角色: 姓名，性别，职业；
import time

roleInformation = []  # 存放所有角色的信息大容器
print('~~~~~~~~~管理系统~~~~~~~~~')
while True:
    choice = input('请选择功能:\n1 添加角色 \n 2 删除角色 \n 3 修改角色 \n 4 查询角色 \n 5 显示所有角色 \n 6 退出\n')
    if choice == '1':
        print('1. 添加角色模块')
        name = input('\t请输入英雄的名字')
        sex = input('\t请输入英雄性别')
        job = input('\t请输入英雄职业')
        listStructureHelp = [name, sex, job]
        roleInformation.append(listStructureHelp)
        print('成功添加{}角色到系统！'.format(name))

    elif choice == '2':
        print('2. 删除角色模块')
        nameDelete = input('请输入要删除的角色名字:')
        for i in roleInformation:
            if nameDelete in i:
                ensure = input('您确定要删除这个角色吗?Y/N')
                if ensure == 'Y' or ensure == 'y':
                    roleInformation.remove(i)
                    print('成功删除{}角色'.format(nameDelete))
                    break
                else:
                    break
            else:
                print('本系统不存在这个名字，请检查！')

    elif choice == '3':
        print('')

    elif choice == '4':
        print('查询角色模块:')
        roleName = input('请输入要查询英雄的名字')
        for i in roleInformation:
            if roleName in i:
                print('角色存在，信息如下:')
                print('{}{}{}'.format(i[0].ljust(10), i[1].ljust(10), i[2].ljust(10)))
                break
            else:
                print('不存在这个角色！')
                break

    elif choice == '5':
        print('5. 查询角色模块')
        print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
        for i in roleInformation:
            print(i[0].center(10), end='')
            print(i[1].center(10), end='')
            print(i[2].center(10), end='')
            print()

    elif choice == '6':
        print('正在退出系统，请耐心等待。。。')
        time.sleep(3)
        print('成功退出')
        break
    else:
        print('输入错误，重新选择!!!!!')
