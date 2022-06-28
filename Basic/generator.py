# 一边循环一遍计算的机制 --> 生成器
# 第一种 通过列表推导式
# newList = [x*3 for x in range(10)]
# print(newList)
# gen = (x*3 for x in range(10))
# print(type(gen))
# print(gen)
#
# # 通过__next__得到元素
# print(gen.__next__())
# print(gen.__next__())
#
# # next()
#
# print(next(gen))

gen = (x*3 for x in range(10))
while True:
    try:
        e = next(gen)
        print(e)
    except:
        print("元素产生完毕，没元素啦")
        break

