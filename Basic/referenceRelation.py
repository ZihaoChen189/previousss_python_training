# import sys
#
# a = 10
# b = a
# c = a
# print(id(a))
# print(id(b))
# print(id(c))
#
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list3 = list1
#
# print(sys.getrefcount(list1))
#
# del list1
# print(sys.getrefcount(list2))
#
# del list3
# print(sys.getrefcount(list2))


# def test(n1):
#     # n1是函数的局部变量，属于这个函数
#     n2 = 100
#     for i in range(n1):
#         print('----->', i)
#     n1 += 1
#
#
# n = 9
# test(n)
# print(n)


list1 = [1, 2, 3]


def test1(l):
    if isinstance(l, list):
        for i in l:
            print('------->', i)
        l.insert(0, 8)
    else:
        print('不是列表类型')


test1(list1)

print(list1)
