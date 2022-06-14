# 集合： 没有重复的，无序的

# 花括号里面没有键值对，那就是集合
# 去除列表里的重复元素: 用集合

# 定义一个集合
# import random
#
# set3 = set()
# print(type(set3))
#
# set1 = {'zihao'}
# set3.add('aaa')
# print(set3)
#
# set1.update(set3)
# print(set1)
#
# code_list = set()
# s = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
# while True:
#     code = ''
#     for i in range(4):
#         r = random.choice(s)
#         code += r
#
#     code_list.add(code)
#
#     if len(code_list) == 5:
#         break
#
# print(code_list)

set1 = set()
set1.pop()  # 随意删除一个元素

# list: 允许重复，有序，有下标
# tuple: 允许重复，里面的元素不能增加删除修改，只能查看
# dict：键值对存在，键是唯一的；值允许重复
# set: 不允许重复，无序 {}
# 相互转换的时候dict把key拿出来转换