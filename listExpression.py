# 人名
# names = ["tom", "john", "jack", "bob", "steven"]
# # 过滤掉长度小于或者等于3的人名
# result = [name for name in names if len(name) > 3]
# result = [name.capitalize() for name in names if len(name) > 3]  # 每个首字母都大写
# print(result)
# newList = []
#
#
# def func(names):
#     for name in names:
#         if len(name) > 3:
#             newList.append(name)
#     return newList
#
#
# result1 = func(names)
# print(result1)

# newList = [i for i in range(1, 101) if i % 3 == 0]
# print(newList)
# newList = []
#
#
# def function():
#     for i in range(5):
#         if i % 2 == 0:
#             for j in range(10):
#                 if j % 2 != 0:
#                     newList.append((i, j))
#     return newList
#
#
# x = function()
# print(x)

# newList = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
# print(newList)
#
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
# newList = [i[-1] for i in list1]
# print(newList)

# dict1 = {'name': 'tom', 'salary': 1000}
# dict2 = {'name': 'alice', 'salary': 4000}
# dict3 = {'name': 'mike', 'salary': 6000}
#
# list1 = [dict1, dict2, dict3]
#
# newList = [person['salary']+200 if person['salary'] > 300 else person['salary']+100 for person in list1]
# print(newList)

# 集合推导式
# list1 = [1, 2, 1, 3, 5, 2, 1, 2, 7, 9, 0, 3, 5]
# set1 = {x+1 for x in list1 if x < 8}  # 在本身的基础上再加1
# print(set1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C'}
newDict = {value: key for key, value in dict1.items()}
print(newDict)