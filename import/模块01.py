# 导入模块
# import calculate
# from calculate import add, number, Calculate
from calculate import *
# 可以通过__all__来制衡这个*符号
list1 = [4, 2, 7, 8, 9]
# result = calculate.add(*list1)
# print(result)
#
# result = calculate.Calculate(1)
# result.test()
# result.test1()
result = add(*list1)
print(result)

s = result + number
print(s)
