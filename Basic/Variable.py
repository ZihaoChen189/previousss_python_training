# money = 28.9  # Declare a variable
# type(money)
# print(type(money))
# generalString = ' '
# print(type(generalString))
# userName = input("请输入用户名")  # 阻塞性语句
#
# print("哈哈哈哈")
# print(userName)
# print(type(userName))
#
# a = 1
# b = 2
# c = 3
#
# print(a + b < c)
#
# result = input("请输入：Y/N")
# if result == "Y":
#     print(4)
#     print("endddddd")
#
# print("---" * 10)

import random
ran = random.randint(1, 10)
print(ran)
guess = int(input("请输入您猜的数字"))  # 键盘输入的是字符串
if ran == guess:  # 9 == "9"
    print("恭喜您！猜对啦")
else:
    print("啊呀，猜错了")
