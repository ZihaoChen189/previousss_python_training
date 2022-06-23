# 全局变量和局部变量
# global 关键字的加入
# 只有一些不可变的类型才需要加global
# 可变的类型不需要添加
a = 100
print(id(a))

a = 90
print(id(a))
# 只要我改变了变量的数值，他的地址也随之改变
# 不可变类型int  str  float  bool  tuple ##########GLOBAL#############

# 可变类型list dict set
s = 'abc'
print(id(s))

s = 'xyz'
print(id(s))
