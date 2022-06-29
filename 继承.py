# # 继承 is a; has a
# import random
#
#
# class Road:
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length
#
#
# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def get_time(self, road):
#         random_time = random.randint(1, 20)
#         message = "{}品牌的车在{}条高速公路上以{}的时速行驶{}小时".format(self.brand, road.name, self.speed, random_time)
#         print(message)
#
#     def __str__(self):
#         return "{}品牌，速度：{}".format(self.brand, self.speed)
#
#
# # 创建实例化对象
# r = Road("京哈高速", 12000)
# r.name = "京广高速"
# car1 = Car("奥迪", 180)
# print(car1)
# print(r.name)
# print(r.length)
# car1.get_time(r)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz


s = Student("珈艺", 17, "python")


