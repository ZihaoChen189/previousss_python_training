list1 = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条']
# pop; remove; clear
# list1.pop(8)  #超出范围了
# pop根据索引删除内容
# remove 根据元素名称删除

# list1. pop()
# # 如果pop没有参数，则是从后往前删除元素
# print(list1)
#
# list1.remove('辣条a')  # 不在list里面
# print(list1)

# 判断是否存在要删除的元素呢 通过关键字in
#
# if '辣条' in list1:
#     print('存在')
# else:
#     print('不存在')

# list1.remove('酸奶')
# print(list1)
# 只能删除一个
#
# for i in list1:
#     if i == '酸奶':
#         list1.remove(i)
# print(list1)
# 全删除了

# 当 有两个连续的元素
# # 考虑用while循环
#
# n = 0
# while n < len(list1):
#     if list1[n] == '酸奶':
#         list1.remove('酸奶')
#     else:
#         n += 1
# print(list1)

# 倒着删除也可以！！！！！

# 修改
list1 = [1, 2, 3, 4, 5, 6]
# list1.insert(1, 8)  # 插队
# print(list1)

weizhi = list1.index(5)
# index 返回值是一个索引位置
list1[weizhi] = 8
print(list1)








