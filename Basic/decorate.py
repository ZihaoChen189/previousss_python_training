# def foo():
#     print("foo")
#
#
# def func():
#     print("func")
#
#
# foo = func
# foo()


# # 定义一个装饰器:
# def decorator(function):
#     print('1')
#
#     def wrapper():
#         function()
#         print("刷漆")
#         print("铺地板")
#         print("买家具")
#         print("精装修")
#     print('2')
#     return wrapper
#
#
# @decorator
# def house():
#     print("毛坯房")
#
#
# decorator()


# 带参数的装饰器
# 如果原函数有参数，则装饰器内部函数也要有参数

# def decorator(function):
#     def inner(*args, **kwargs):
#         # ******Args是一个元祖，是一个整体，上下这两个都要加****Args
#         function(*args, **kwargs)
#         print("刷漆")
#         print("铺地板")
#         print("买家具")
#         print("精装修")
#     return inner
#
#
# @decorator
# def house(address):
#     print("房子的地址在{}，是一个毛坯房".format(address))
#
#
# @decorator
# def changfang(address, area):
#     print("房子的地址在{}，是一个毛坯房，建筑面积是{}".format(address, area))
#
#
# @decorator
# def hotel(name, address, area=40):
#     print("房子的地址在{}，是一个酒店，名字是{}，单间面积是{}".format(address, name, area))
#
#
# house('北京四合院')
# changfang('天安门', 960)
# hotel(name='四季酒店', address='国贸')


# #######带返回值的装饰器
def decorator(function):
    def inner(*args, **kwargs):
        r = function(*args, **kwargs)
        print("预计装修费用{}".format(r))
        print("刷漆")
        print("铺地板")
        print("买家具")
        print("精装修")
        return r
    return inner


@decorator
def house():
    print("我是一个毛坯房。。。")
    return 5000


r = house()

print(r)
