# 在开发中看到一些私有化处理：装饰器
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    # def set_age(self, age):
    #     self.__age = age
    #
    # def get_age(self):
    #     return self.__age

    @property
    def age(self):
        return self.__age
    # 先定义get，之后才能用set

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return "姓名：{}，年龄：{}".format(self.name, self.__age)


s1 = Student("珈艺", 20)
s1.name = "佳艺"
s1.age = 21
print(s1.age)
