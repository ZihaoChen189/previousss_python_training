"""
匿名函数的使用场合
1. 匿名函数作为参数使用
"""
from functools import reduce


def test():
    print("----test----")


def func(a, f):
    print("---->", a)
    f()


func(5, test)

print("---------分割线")


def func1(a, f):
    print("++++++>", a)
    r = f(a)
    print(r)


func1(8, lambda x: x**2)

# 高阶函数：一个函数的参数是另一个函数 sorted, max, min
m = max(5, 9)
print(m)

list11 = [('Tom', 19), ('Alice', 20), ('Lily', 21), ('Rose', 19)]
m = max(list11, key=lambda x: x[1])
print(m)

mi = min(list11, key=lambda x: x[1])
print(mi)

s = sorted(list11, key=lambda x: x[1], reverse=True)
print(s)

# filter的匿名函数要求返回值必须是boolean类型，只有boolean类型结果为True的才是符合过滤条件的
rr = filter(lambda x: x[1] > 20, list11)
print(list(rr))

# list2 = []
# for i in list11:
#     if i[1] > 20:
#         list2.append(i)

m1 = map(lambda x: x[1]+1, list11)
print(list(m1))

m1 = map(lambda x: x[0].upper(), list11)
print(list(m1))

r = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(r)
