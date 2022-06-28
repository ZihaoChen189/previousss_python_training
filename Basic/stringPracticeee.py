# s = 'https://studentnet.cs.manchester.ac.uk/ugt/choices.php?programme=%23SPLUS4BB7C2&year=2021&currentyear=2021'
#
# result = s.startswith('www.')
# result_1 = s.startswith('http')
# print(result)
# result_2 = s.endswith('2021')
# # print(result_2)

# import random
# file = input('请输入文件的全称：')
# if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
#     # 再判断文件名字
#     i = file.rfind('.')
#     name = file[:i]
#     if len(name) < 6:
#         # 重新构造
#         n = random.randint(100000, 999999)
#         new_name = str(n) + file[i:]
#         print('成功上传%s文件' % new_name)
#
# else:
# #     print('文件格式错误！')
#
# # 字母数字组合
# import random
#
# filename =  ' '
# s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
# for i in range(6):
#     index = random.randint(0, len(s) - 1)
#     filename += s[index]
# print(filename)


# import random
# s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
# file = input('请输入文件的全称：')
#
# if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
#     # 再判断文件名字
#     i = file.rfind('.')  # 找到了点的位置
#     name = file[:i]  # 不包括点的名字
#     if len(name) < 6:
#         filename = ''
#         for a in range(4):
#             index = random.randint(0, len(s) - 1)
#             filename += s[index]
#             newFile = filename + file[i:]
#         print(newFile)
#
# else:
#     print('文件格式错误')
#
# s = 'A123456789'
# anwer = s.isalpha()
# anwer_1 = s.isalnum()
# print(anwer)
# print(anwer_1)

flag = True
while flag:
    name = input('用户名/手机号码:')
    # 判断
    if(name.islower() and not name[0].isdigit() and len(name) > 6) or (name.isdigit() and len(name) == 11):
        while True:
            password = input('请输入密码')
            if len(password) == 6 and password.isdigit():
                if name == 'admin123' and password == '123456':
                    print('登录成功')
                    flag = False
                    break
                else:
                    print('用户名或者密码有误！')
                    break
            else:
                print('密码格式不对呀')
    else:
        print('用户名或者密码格式错误')