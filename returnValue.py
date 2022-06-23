# def get_sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
#
#
# t = get_sum(1, 2, 3)
# x = 100
# x += t
# print(x)


# def get_max_min(numbers):
#     # 先排序
#     for i in range(0, len(numbers) - 1):
#         for j in range(0, len(numbers) - 1 - i):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     minvalue = numbers[0]
#     maxvalue = numbers[-1]
#     return minvalue, maxvalue
#
#
# list1 = [34, 11, 78, 90, 100, 23, 56, 88, 91]
# a, b = get_max_min(list1)
# print(a, b)

# 全局变量和局部变量
# global 关键字的加入
# 只有一些不可变的类型才需要加global
# 可变的类型不需要添加
