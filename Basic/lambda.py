"""
用lambda创建小型匿名函数，省略了def声明函数的过程
定义格式：
lambda 参数列表：返回值运算表达式
"""


# def test(a):
#     return a + 1
#
#
# result = lambda a : a + 1
# result(9)

r = lambda x, y: x+y
result = r(1, 2)
print(result)
