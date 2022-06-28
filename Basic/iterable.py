from collections.abc import Iterable
# 可迭代的对象：生成器；元祖；列表；集合；字典；字符串
list1 = [1, 4, 7, 8, 8]
f = isinstance(list1, Iterable)
g = isinstance('abc', Iterable)
h = isinstance(100, Iterable)
print(f)
print(g)
print(h)

g = (x+1 for x in range(10))
result = isinstance(g, Iterable)
print(result)

# 迭代器 只能往前，不能往后
# 可以被next()函数调用并不断返回下一个数值的对象称之为 迭代器
# 可迭代的对象一定是迭代器？
# 列表就不是！但他是可迭代的，从开头遍历到最后

list1 = iter(list1)
print(next(list1))
# ------>可以通过iter(xxx)把可迭代的对象变成一个迭代器

