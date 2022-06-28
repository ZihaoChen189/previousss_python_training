# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     # 删除引用
#     def __del__(self):
#         print("DELETE******************")
#
#
# p = Person("珈艺")
# p1 = p
# p2 = p
# # 大哥二哥三哥在一家
# del p2
# del p1

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "姓名是：" + self.name


p = Person("珈艺")
print(p)
# 单纯打印对象名称，是一个地址，对于开发者来说，没有太大意义
# 如果想打印对象名字的时候，给开发者更多信息量
# 触发条件：当打印一个对象名字的时候，自动触发调用str里的内容
# ########一定一定  加 RETURN！！！！！！！！！！
