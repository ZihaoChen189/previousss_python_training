# class Person:
#     name = "jiayi"
#
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#
# p1 = Person(12, "zihao")
# print(p1.age)
# print(p1.name)

# 类方法


# class Dog:
#     name = "aa"
#
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print("{}在院子里跑来跑去".format(self.name))
#
#     @classmethod  # 类方法
#     def test(cls):  # class的简写  cls  ----->    Dog   把类变成参数
#         # 类方法中，只能使用对象属性
#         # 在类方法中，因为只能访问类属性和类方法，可以在对象创建之前做一些动作，功能
#         print(Dog.name)
#
#
# # d = Dog("大黄")
# # d.test()
# Dog.test()
# # d.run()


"""
summary:  类方法；静态方法
不同：
    1 装饰器不同
    2 类方法是有参数的；静态方法没有参数
相同：
    1 都可以通过类名.    访问
    2 只能访问类的属性和方法，对象是无法访问的
    3 在没有对象前使用，不依赖于对象
    
普通方法与两者之区别：
不同：
没有装饰器；普通方法永远依赖对象，有那个self

"""


class Cat:
    type = "猫"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food):
        print("{}喜欢吃{}".format(self.name, food))

    def catch_mouse(self, color, weight):
        print("{}抓了一只{}颜色的，{}大的老鼠".format(self.name, color, weight))

    def sleep(self, hour):
        if hour < 5:
            print("宝子{}，继续睡叭".format(self.name))
        else:
            print("这个年纪你怎么睡得着？")

    def show(self):
        print("猫的信息：")
        print(self.name, self.age, self.color)


cat1 = Cat("珈艺", 18, "粉色")
cat1.catch_mouse("黑色", 5)
cat1.sleep(1)
cat1.eat("鱼")
cat1.show()