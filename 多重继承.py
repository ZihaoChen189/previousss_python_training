# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("eatttttt")
#
#     def eat(self, food):
#         print(food)
#
#
# p = Person("hhh")
# p.eat("狮子头")

class A:
    def test(self):
        print("AAAAAA")


class B:
    def test1(self):
        print("BBBBBBB")


class C(A, B):
    def test2(self):
        print("CCCCCCC")


c = C()
c.test()
c.test1()
c.test2()
print(C.__mro__)
# python允许多继承
# 如果父类当中
