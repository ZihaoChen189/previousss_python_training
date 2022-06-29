class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz


class Employee(Person):
    def __int__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


e = Employee("珈艺", 18, "s")





