"""
单例模式，各种开发模式
开发模式：单例模式 ---> 单个对象
不需要开辟太多的内存空间
"""


# class Student:
#     pass
#
#
# s = Student()
# s1 = Student()
# print(s)
# print(s1)


class Singeleton:
    # 私有化当前类的实例
    __instance = None
    name = "珈艺"

    # 重写__new__
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def show(self, n):
        print(Singeleton.name, n)


s = Singeleton()
s1 = Singeleton()
print(s)
print(s1)
s.show(6)
s1.show(4)
