# 语法错误和异常

# while True:
#     print("~~~~~")


# number = 100
# def func():
#     # global number
#     number += 1


# 异常,程序运行的时候报出来。。。。。。Error
# def divide(a, b):
#     return a/b
#
#
# divide(1, 0)  # ZeroDivisionError: division by zero

# 处理异常
"""
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
finally:
    无论有没有异常，都会执行的代码（可有可无）
"""


# def func():
#     try:
#         n1 = int(input("请输入第一个数字"))
#         n2 = int(input("请输入第二个数字"))
#         operation = input("请输入运算符号+-*/")
#         if operation == '+':
#             s = n1 + n2
#         elif operation == '-':
#             s = n1 - n2
#         elif operation == '*':
#             s = n1 * n2
#         elif operation == '/':
#             s = n1 / n2
#         else:
#             print("符号输入有误！！！！！")
#         print("结果是", s)
#      except ZeroDivisionError:
#         print("除数不能为零")
#     except ValueError:
#         print("输入的值必须是数字")
#
#
# func()

# object -> BaseException -> Exception -> 开花

# 想知道真正的报错原因，具体：
# except Exception as err:
#     print(err)
# try:
#     list1 = []
#     list1.pop()
# except Exception as err:
#     print(err)

"""
文件操作： stream = open(); stream.read(); stream.close() 不管有没有问题，你得先关闭！！！！！！！
对应try; except; finally
"""

# ###try######里的return并不会真正执行！！！！finally里的return才是最重要的！！！！！！！！！！！！！
# finally 特殊情况特殊考虑

# 抛出异常


def register():
    username = input()
    if len(username) < 6:
        raise Exception("用户长度必须六位以上")
    else:
        print("输入的用户名", username)


try:
    register()
except Exception as err:
    print(err)
    print("注册失败")
else:
    print("注册成功")
    