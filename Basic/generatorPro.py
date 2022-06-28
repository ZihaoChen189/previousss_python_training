# 借助函数定义生成器
# 只要出现yield！就不是函数了，而是生成器


# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # 定义生成器！！！！！！！！！！return n + 暂停
#         # print(n)
#
#
# g = func()
# # print(g)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def fib(length):
#     a, b = 0, 1
#     n = 0
#     while n < length:
#         # print(b)
#         yield b
#         a, b = b, a+b
#         n += 1
#
#
# g = fib(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print("temp->", temp)
#         i += 1
#     return "没有更多数据"
#
#
# g = gen()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# print(g.send(None))
# n1 = g.send("呵呵")
# print("n1--->", n1)
# n2 = g.send("哈哈")
# print("n2--->", n2)

"""
生成器方法：
__next__() 获取下一个元素
send(value): 向每次生成器调用中传值，第一次必须传递一个None
"""


def task1(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i))
        yield None


def task2(m):
    for j in range(m):
        print("正在听第{}块歌".format(j))
        yield None


g1 = task1(5)
g2 = task2(5)

# while True:
#     try:
#         g1.__next__()
#         g2.__next__()
#     except:
#         pass


"""
生成器generator
定义方式：1通过列表推倒式 g = (x for x in range(6))
                  2借助函数+yield 
                  def func():
                      ...
                      yield
                
                g = func()
                产生：
                1. next(generator)
                2. g.__next__() :元素产生完毕，再次调用的话，就会产生异常
                3. g.send(None/VAlue)
                应用：：：：：
                 协程
"""