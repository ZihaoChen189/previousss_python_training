# # in 查找 返回一个bool
# # index 返回元素的下标位置
# # list1 = [1, 2, 3, 4, 5]
# # del list1[3]
# # list1.pop(3)
# # clear之后还是可以往列表里添加
# # 但是del 是真的删除了del list1
#
# # 生成8个1-20之间的随机整数，保存在列表中print
#
# import random
# numbers = []
# for i in range(8):
#     randomDigit = random.randint(1, 20)
#     numbers.append(randomDigit)
# print(numbers)
# # numbers.sort(reverse=True)
# # # 默认是False 生序  控制reverse=的参数控制
# # print(numbers)
# # numbers.reverse()
# # print(numbers)  # 单纯反转
#
# numbers.sort()
# num = int(input('请输入要插入的数值'))
# numbers.append(num)
# numbers.sort()
# print(numbers)

a = 1
b = 2
a, b = b, a
print(a, b)

a = 1
b = 3
c = a
a = b
b = c
print(a, b)




