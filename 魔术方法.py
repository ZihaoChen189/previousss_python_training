# 魔术方法
# __init__

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# p = Person("Jiayi Guo")

# __new__(): 实例化的魔术方法
# 触发时机: 在实例化时触发
class Person:
    def __init__(self, name):
        print("init")
        self.name = name

    def __new__(cls, *args, **kwargs):  # 向内存要一个地址空间  ------>
        print("new")
        # object.__new__(cls, *args, **kwargs)
        return object.__new__(cls)

    def __call__(self, name):  # 把对象当作函数调用时触发，会默认调用次函数中的内容
        print("call,参数是", name)


# p = Person("Jiayi Guo")
# print(p.name)  # 报错了？？？？？？？为什么？？？？？？
# 原因: 那个new烦人，print(p)都变成None了，情况很严重
# print(p)

p = Person("aaa")
print(p)
p("hello")
