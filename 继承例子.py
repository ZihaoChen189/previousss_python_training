class Person:
    def __init__(self, number, name, salary):
        self.number = number
        self.name = name
        self.salary = salary

    def __str__(self):
        message = "工号：{}，姓名：{}，本月工资：{}".format(self.number, self.name, self.salary)
        return message

    def get_salary(self):
        return self.salary


class Worker(Person):
    def __init__(self, number, name, salary, worktime, per_hour):
        super().__init__(number, name, salary)
        self.worktime = worktime
        self.per_hour = per_hour

    def get_salary(self):
        money = self.worktime * self.per_hour
        self.salary += money
        return self.salary


class Salesman(Person):
    def __init__(self, number, name, salary, sale_money, percent):
        super().__init__(number, name, salary)
        self.sale_money = sale_money
        self.percent = percent

    def get_salary(self):
        money = self.sale_money * self.percent
        self.salary += money
        return self.salary


# 创建子类对象
w = Worker("0001", "珈艺", 2000, 160, 100)
print(w.get_salary())

s = Salesman("0002", "紫灏", 5000, 5000000, 0.003)
print(s.get_salary())
