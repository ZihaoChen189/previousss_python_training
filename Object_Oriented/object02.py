class Student:
    # 类属性
    name = "ZihaoChen"
    age = 2


# 创建对象
# 对象 = 类名()
zihao = Student()
print(zihao.age)
zihao.age = 18
print(zihao.age)

Student.age = 18
print(zihao.age)
Jiayi = Student()
print(Jiayi.age)


"""
列表表达式：[表达式 for 变量 in 列表]
[x+2 for x in list1]  -->  新的列表

[表达式 for 变量 in 列表 if 条件]
[x+2 for x in list1 if x%2 == 0]

[结果A if 条件 else 结果B for x in list1]
字典推导式：{key, value for k, v in 字典.items()}


生成器generator：
    1. 使用类似的列表推导式 g = (表达式 for 变量 in 列表)
                                    此时的g就是生成器
    2. 函数+yield
                    next(g)   ; __next__()   send(None), send(1, 2...)
                    
是否可迭代：
isinstance(x, Iterable)
list是可迭代的，但不是迭代器，咋么办
iter(list)

"""