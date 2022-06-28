class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 90
    # 定义共有的set和get
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def __str__(self):
        return "姓名：{}，年龄：{}，考试分数：{}".format(self.__name, self.__age, self.__score)


jiayi = Student("珈艺", 18)
print(jiayi)
jiayi.setAge(19)
print(jiayi)
print(jiayi.getAge())
#
# jiayi.age = 19
# jiayi.__score = 93

# 私有化：封装的思想 ---> 私有化属性，定义共有set和get方法
# 可以隐藏咱们的属性，不被外界随意更改

